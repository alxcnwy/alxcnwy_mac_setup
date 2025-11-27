#!/usr/bin/env python3
"""
backup_chatgpt.py

Local helper to export Codex CLI / ChatGPT session history from the Codex CLI
session log directory into a simple, human-readable text archive plus a
structured JSONL mirror.

What it does:
- Reads `.jsonl` session files under `~/.codex/sessions` (written by Codex CLI).
- Writes `.txt` files into `~/Documents/_____db/chatgpt/txt`, one per session,
  with timestamps and event payloads for easier grepping and manual review.
- Copies the raw `.jsonl` session files into
  `~/Documents/_____db/chatgpt/jsonl` using the same timestamp/session-id based
  naming scheme, so you keep a structured archive too.

How to run:
- One-shot backup (manual):
    python3 backup_chatgpt.py
- Lightweight "watch" mode (runs every N seconds, default 15, only re-processing
  new or changed session files in memory):
    python3 backup_chatgpt.py --watch
    python3 backup_chatgpt.py --watch --interval 15

For long-running background use, you can:
- Start `--watch` in its own terminal tab, or
- Call this script from your `codexx` wrapper after each Codex run.

Disclaimers:
- This script only touches local files; it does not call any OpenAI APIs
  or access remote services. It will happily run completely offline.
- Exported files may contain sensitive or personal data. You are responsible
  for how and where you store them and for complying with any company
  policies and OpenAI’s Terms of Use.
- This is not official OpenAI software; use at your own risk.
"""

from pathlib import Path
from datetime import datetime
import argparse
import json
import time
import shutil


# Source and destination
# Codex CLI stores sessions under ~/.codex/sessions as nested year/month/day dirs
SRC = Path.home() / ".codex" / "sessions"
DEST = Path.home() / "Documents" / "_____db" / "chatgpt"
DEST.mkdir(parents=True, exist_ok=True)
DEST_TXT = DEST / "txt"
DEST_JSONL = DEST / "jsonl"
DEST_TXT.mkdir(parents=True, exist_ok=True)
DEST_JSONL.mkdir(parents=True, exist_ok=True)


def safe(s: str) -> str:
    return "".join(c for c in s if c.isalnum() or c in "-_.")


def iter_session_files(src_root: Path):
    """Yield all .jsonl session files under the Codex sessions directory."""
    if not src_root.exists():
        return
    yield from src_root.rglob("*.jsonl")


def export_sessions(seen_files=None) -> int:
    """
    Export all sessions under SRC into DEST.

    If `seen_files` is a dict mapping Path -> mtime, only new/changed files
    are processed. Returns the number of session files written this run.
    """
    written = 0

    for session_file in iter_session_files(SRC):
        try:
            mtime = session_file.stat().st_mtime
        except OSError:
            continue

        if seen_files is not None:
            last_mtime = seen_files.get(session_file)
            if last_mtime is not None and mtime <= last_mtime:
                continue
            seen_files[session_file] = mtime

        session_id = None
        created_iso = None
        events = []

        with open(session_file, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    ev = json.loads(line)
                except Exception:
                    continue

                ts = ev.get("timestamp")
                typ = ev.get("type")
                payload = ev.get("payload")

                if session_id is None and typ == "session_meta":
                    meta = payload or {}
                    session_id = meta.get("id") or session_file.stem
                    created_iso = meta.get("timestamp") or ts

                events.append((ts, typ, payload))

        if not events:
            continue

        if session_id is None:
            session_id = session_file.stem

        if created_iso is None:
            created_iso = events[0][0]

        try:
            created_dt = datetime.fromisoformat(created_iso.replace("Z", "+00:00"))
            created_str = created_dt.strftime("%Y-%m-%d_%H-%M-%S")
        except Exception:
            created_str = "unknown"

        base_name = f"{created_str}__{safe(session_id)}"
        txt_name = f"{base_name}.txt"
        jsonl_name = f"{base_name}.jsonl"
        out_txt_path = DEST_TXT / txt_name
        out_jsonl_path = DEST_JSONL / jsonl_name

        lines = []
        lines.append(f"SESSION_FILE: {session_file}")
        lines.append(f"SESSION_ID: {session_id}")
        lines.append(f"CREATED_AT: {created_iso}")
        lines.append("")

        for ts, typ, payload in events:
            lines.append(f"--- {ts} | {typ} ---")

            if isinstance(payload, dict):
                try:
                    lines.append(json.dumps(payload, indent=2))
                except Exception:
                    lines.append(str(payload))
            else:
                lines.append(str(payload))
            lines.append("")

        with open(out_txt_path, "w") as f:
            f.write("\n".join(lines))

        # Also mirror the raw JSONL session into the jsonl subfolder so we keep
        # a structured archive alongside the human-readable export.
        try:
            shutil.copy2(session_file, out_jsonl_path)
        except OSError:
            # If copying fails, we still count the session as written because
            # the txt export succeeded; JSONL mirroring is best-effort.
            pass

        written += 1

    return written


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Export Codex CLI / ChatGPT sessions from ~/.codex/sessions into "
            "human-readable text files under ~/Documents/_____db/chatgpt/txt "
            "and mirrored JSONL files under ~/Documents/_____db/chatgpt/jsonl."
        ),
    )
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Run in a loop, exporting new/changed sessions every INTERVAL seconds.",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=15,
        help="Seconds between runs in --watch mode (default: 15).",
    )
    args = parser.parse_args()

    if not args.watch:
        written = export_sessions()
        print(
            f"Export complete. Text files in: {DEST_TXT}, "
            f"JSONL copies in: {DEST_JSONL} (sessions written: {written})"
        )
        print(
            "Note: these exports may contain sensitive data. "
            "Handle and back them up in line with your own privacy, security, "
            "and OpenAI usage policies."
        )
        return

    interval = max(1, args.interval)
    print(
        f"[backup_chatgpt] Watching {SRC} every {interval} seconds. "
        f"Writing text exports to {DEST_TXT} and JSONL copies to {DEST_JSONL}. "
        f"Press Ctrl+C to stop."
    )
    seen_files = {}

    try:
        while True:
            written = export_sessions(seen_files)
            if written:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(
                    f"[{now}] Exported {written} session(s). "
                    f"Latest files are in: {DEST}"
                )
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[backup_chatgpt] Stopped watch mode.")
        print(
            "Note: exported files may contain sensitive data. "
            "Handle and back them up in line with your own privacy, security, "
            "and OpenAI usage policies."
        )


if __name__ == "__main__":
    main()
