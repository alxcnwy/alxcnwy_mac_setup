Snapshot Tabs to Datestamped Folder
🧩 Overview

Snapshot Tabs to Datestamped Folder is a minimalist Chrome extension that saves all open tabs from your currently focused Chrome window into a neatly labeled folder inside your bookmarks.

Each snapshot is stored under the parent SNAPSHOTS folder, with subfolders automatically named using the current date, time, and tab count — e.g.:

Bookmarks
└── SNAPSHOTS
    ├── 11-11-2025 14-37 [8]
    │   ├── GitHub
    │   ├── Gmail
    │   └── Notion


Use it as your “instant brain dump” when context-switching or clearing windows without losing progress.

⚙️ Features

Saves only the active Chrome window’s tabs

Skips internal pages (e.g. chrome://)

Organizes snapshots under Bookmarks → SNAPSHOTS

Folder automatically named:
DD-MM-YYYY HH-MM [N]

Default shortcut: Cmd + Shift + 0 (macOS) / Alt + Shift + 0 (Windows)

Brief visual feedback: temporary highlight of the new folder

🚀 Installation

Download or clone this folder.

Visit chrome://extensions

Enable Developer Mode (top right).

Click Load unpacked → select your snapshot_tabs folder.

Open any Chrome window with multiple tabs.

Press Cmd + Shift + 0 (macOS) or Alt + Shift + 0 (Windows).

Check Bookmarks → SNAPSHOTS for your saved session.

🔔 Visual Feedback (Optional Notification)

Add this small snippet at the end of your background.js to get a native Chrome notification confirming each snapshot:

await chrome.notifications.create({
  type: "basic",
  iconUrl: "icon128.png", // optional
  title: "Snapshot Saved",
  message: `Saved ${tabs.length} tabs → SNAPSHOTS/${folderName}`,
  priority: 1
});


Then add "notifications" to your permissions array in manifest.json:

"permissions": ["bookmarks", "tabs", "notifications"]


This gives a quick pop-up for 2–3 seconds — ideal lightweight feedback that your snapshot succeeded.

🧠 Tips

You can change the shortcut anytime at:
chrome://extensions/shortcuts

Want per-project snapshots? Rename folders or prefix them manually (e.g. “ClientA – 11-11-2025 14-40 [12]”).

Combine with Chrome’s Memory Saver or OneTab for even cleaner tab hygiene.