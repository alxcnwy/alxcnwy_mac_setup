#!/usr/bin/env python3
"""
sync_bettertouchtool.py

Helper script to sync your local BetterTouchTool configuration into this repo.

By default (no flags), it makes a safe snapshot copy of:
    ~/Library/Application Support/BetterTouchTool
into:
    <repo_root>/app_config_files/bettertouchtool/live

This does NOT modify your BetterTouchTool installation and can be run
whenever you want to refresh the snapshot in the repo.

Advanced mode:
    --link --force

This will:
    - Move the BetterTouchTool config directory into the repo, then
    - Replace the original directory with a symlink pointing back here.

After that, any changes made by BetterTouchTool are stored directly inside
the repo (and thus show up in git). This is more invasive and should only be
used after quitting BetterTouchTool completely.
"""

from __future__ import annotations

from pathlib import Path
import argparse
import os
import shutil
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
BTT_DIR = Path.home() / "Library" / "Application Support" / "BetterTouchTool"
DEST_DIR = REPO_ROOT / "app_config_files" / "bettertouchtool" / "live"


def copy_config() -> int:
    """Copy the current BetterTouchTool config into the repo."""
    if not BTT_DIR.exists():
        print(f"[ERROR] BetterTouchTool directory not found: {BTT_DIR}")
        return 1

    if DEST_DIR.exists():
        print(f"[INFO] Removing existing snapshot: {DEST_DIR}")
        shutil.rmtree(DEST_DIR)

    DEST_DIR.parent.mkdir(parents=True, exist_ok=True)

    print(f"[INFO] Copying {BTT_DIR} -> {DEST_DIR}")
    shutil.copytree(BTT_DIR, DEST_DIR)
    print("[OK] Snapshot updated.")
    return 0


def link_config(force: bool = False) -> int:
    """
    Move the BetterTouchTool config directory into the repo and replace the
    original with a symlink.

    This is destructive in the sense that it moves/removes the original
    directory under ~/Library/Application Support, so it requires --force.
    """
    if not BTT_DIR.exists() and not BTT_DIR.is_symlink():
        print(f"[ERROR] BetterTouchTool directory not found: {BTT_DIR}")
        return 1

    if BTT_DIR.is_symlink():
        target = BTT_DIR.resolve()
        print(f"[INFO] BetterTouchTool directory is already a symlink -> {target}")
        return 0

    if not force:
        print(
            "[ABORT] --link is an invasive operation.\n"
            "Quit BetterTouchTool first, then re-run with:\n"
            "    python3 scripts/sync_bettertouchtool.py --link --force\n"
            f"This will move:\n  {BTT_DIR}\ninto:\n  {DEST_DIR}\n"
            "and replace the original with a symlink.",
        )
        return 1

    if not DEST_DIR.exists():
        DEST_DIR.parent.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Moving {BTT_DIR} -> {DEST_DIR}")
        shutil.move(str(BTT_DIR), str(DEST_DIR))
    else:
        print(
            f"[INFO] Destination already exists: {DEST_DIR}\n"
            "Will remove the original BetterTouchTool directory and "
            "point it at the existing destination.",
        )
        if BTT_DIR.exists():
            print(f"[INFO] Removing existing BetterTouchTool directory: {BTT_DIR}")
            shutil.rmtree(BTT_DIR)

    print(f"[INFO] Creating symlink {BTT_DIR} -> {DEST_DIR}")
    os.symlink(str(DEST_DIR), str(BTT_DIR))
    print("[OK] BetterTouchTool now uses the repo-backed config directory.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Sync BetterTouchTool configuration into this repo.\n\n"
            "Default: make a snapshot copy under app_config_files/bettertouchtool/live.\n"
            "Use --link --force to move the config into the repo and "
            "symlink the original directory."
        )
    )
    parser.add_argument(
        "--link",
        action="store_true",
        help="Move BetterTouchTool config into the repo and symlink the original directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Required together with --link to actually perform the move/symlink.",
    )

    args = parser.parse_args()

    if args.link:
        return link_config(force=args.force)
    return copy_config()


if __name__ == "__main__":
    sys.exit(main())

