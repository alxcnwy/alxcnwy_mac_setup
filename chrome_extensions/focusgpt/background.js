// Ensure "SNAPSHOTS" folder exists or create it
async function getOrCreateSnapshotsFolder() {
  const results = await chrome.bookmarks.search({ title: "SNAPSHOTS" });
  if (results && results.length > 0) return results[0];
  return await chrome.bookmarks.create({ title: "SNAPSHOTS" });
}

// Create a timestamp string like "11-11-2025 14-32"
function getTimestamp() {
  const now = new Date();
  const date = now.toLocaleDateString("en-GB").replace(/\//g, "-");
  const time = now
    .toLocaleTimeString("en-GB", { hour12: false })
    .replace(/:/g, "-");
  return `${date} ${time}`;
}

// Listen for keyboard shortcut command
chrome.commands.onCommand.addListener(async (command) => {
  if (command !== "save_tabs") return;

  try {
    // Focused window only
    const currentWindow = await chrome.windows.getCurrent({ populate: true });
    const tabs = currentWindow.tabs.filter(
      (t) => t.url && !t.url.startsWith("chrome://")
    );

    const timestamp = getTimestamp();
    const snapshotsFolder = await getOrCreateSnapshotsFolder();
    const folderName = `${timestamp} [${tabs.length}]`;

    const snapshotFolder = await chrome.bookmarks.create({
      parentId: snapshotsFolder.id,
      title: folderName
    });

    for (const tab of tabs) {
      await chrome.bookmarks.create({
        parentId: snapshotFolder.id,
        title: tab.title || tab.url,
        url: tab.url
      });
    }

    console.log(`✅ Saved ${tabs.length} tabs → SNAPSHOTS/${folderName}`);

    // 🔔 Chrome notification (non-await, callback style)
    chrome.notifications.create({
      type: "basic",
      iconUrl: "icon128.png",
      title: "Snapshot Saved",
      message: `Saved ${tabs.length} tabs → SNAPSHOTS/${folderName}`,
      priority: 1
    });
  } catch (error) {
    console.error("❌ Error saving snapshot:", error);
  }
});
