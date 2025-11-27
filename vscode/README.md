## VS Code configuration and extensions

### Tabs instead of sidebar

Goal: focus on editor tabs instead of the sidebar, and use a simple toggle:

- Use `Cmd+B` to hide/show the sidebar.
- Enable tabs and disable preview so tabs don’t auto-replace.

In VS Code settings (`settings.json` or the UI):

- Set `workbench.editor.showTabs` to `true`.
- Set `workbench.editor.enablePreview` to `false`.
- (Optional) For a cleaner layout in Zen Mode:
  - `workbench.editor.showTabs`: `true`
  - `window.menuBarVisibility`: `"compact"`

These can be represented in `settings.json` like:

```jsonc
{
  // Show editor tabs
  "workbench.editor.showTabs": true,

  // Don’t auto-replace the active tab
  "workbench.editor.enablePreview": false,

  // Optional: compact menu bar
  "window.menuBarVisibility": "compact"
}
```

Combine with Zen Mode (`Cmd+K Z`) and `Cmd+B` to quickly toggle the sidebar while leaving tabs visible.

### Codex Status VS Code extension (status dot)

Goal: show a grey/green/red dot in the status bar based on Codex CLI runtime status, driven by a small local file (`~/.codex_status`) that any script can update.

This repo contains a minimal VS Code extension under `vscode/codex-status/`:

- Adds a status bar icon (●) on the left.
- Reads `~/.codex_status` and sets color:
  - `idle` → grey
  - `running` → green
  - `error` → red

#### Files

- `vscode/codex-status/extension.js`
- `vscode/codex-status/package.json`

#### Developing / running the extension

From this repo:

```bash
cd "$HOME/Documents/_____setup/alxcnwy_mac_setup/vscode/codex-status"
npm install
code .
```

In the VS Code window that opens:

- Press `F5` to launch an Extension Development Host with the extension active.
- You should see a ● in the status bar.

#### Status file

The extension watches `~/.codex_status`:

- `"idle"` → grey
- `"running"` → green
- `"error"` → red
- Anything else / missing file → grey

You can update this file from any script:

```bash
echo "running" > ~/.codex_status
echo "idle" > ~/.codex_status
echo "error" > ~/.codex_status
```

#### Codex CLI wrapper script

Create a small wrapper script that updates `~/.codex_status` around Codex CLI runs:

```bash
mkdir -p "$HOME/bin"

cat <<'EOF' > "$HOME/bin/codexx"
#!/bin/zsh
echo "running" > "$HOME/.codex_status"
codex "$@"
if [ $? -eq 0 ]; then
    echo "idle" > "$HOME/.codex_status"
else
    echo "error" > "$HOME/.codex_status"
fi
EOF

chmod +x "$HOME/bin/codexx"
```

Ensure `~/bin` is on your `PATH` (e.g. via your shell config), then use `codexx` instead of `codex`. The status dot in VS Code will now reflect Codex CLI status.

### Codex history backup script

To keep a plain-text archive of your Codex CLI / ChatGPT sessions, this repo includes `scripts/backup_chatgpt.py`:

- Reads session `.jsonl` files from `~/.codex/sessions`.
- Writes human-readable `.txt` files into `~/Documents/_____db/chatgpt` with timestamps and events per session.

Run it from this repo:

```bash
cd "$HOME/Documents/_____setup/alxcnwy_mac_setup"
python3 scripts/backup_chatgpt.py
```
