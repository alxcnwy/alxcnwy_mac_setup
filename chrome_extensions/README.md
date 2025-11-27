# Chrome Extensions

This folder contains small, focused Chrome extensions that live in this setup repo so they can be re-used on new machines.

## Extensions

- `focusgpt`
  - Name in Chrome: **FocusGPT Snapshot**
  - Purpose: one-key “focus snapshot” that saves all tabs in the current Chrome window into `Bookmarks → SNAPSHOTS → <timestamp> [tabcount]` with a desktop notification.
  - Default shortcut: `Cmd+Shift+0` (macOS) / `Alt+Shift+0` (Windows).

- `save_tabs_in_window_to_timestamped_bookmarks_folder`
  - Name in Chrome: **Snapshot Tabs to Datestamped Folder**
  - Purpose: earlier version of the same idea; saves the active window’s tabs into `Bookmarks → SNAPSHOTS → <timestamp> [tabcount]`.
  - Default shortcut: `Cmd+Shift+0` (macOS) / `Alt+Shift+0` (Windows).

## Install (unpacked)

For either extension:

1. Open Chrome and go to `chrome://extensions`.
2. Turn on **Developer mode** (top-right).
3. Click **Load unpacked**.
4. Select the folder for the extension you want:
   - `chrome_extensions/focusgpt`
   - or `chrome_extensions/save_tabs_in_window_to_timestamped_bookmarks_folder`

The extension will appear in your toolbar or under the extensions menu.

## Use / Test Quickly

1. Open a Chrome window with a few tabs you care about.
2. Trigger the shortcut:
   - `Cmd+Shift+0` on macOS
   - `Alt+Shift+0` on Windows
3. Open your bookmarks and navigate to `Bookmarks → SNAPSHOTS`.
4. You should see a new folder named like `11-11-2025 14-37 [8]` containing bookmarks for each tab.

If the shortcut doesn’t fire:

- Go to `chrome://extensions/shortcuts`.
- Find the extension’s command (e.g. **FocusGPT Snapshot – save_tabs**).
- Rebind it to your preferred key combo if needed.

