const vscode = require('vscode');
const fs = require('fs');
const path = require('path');

function activate(context) {
    const statusItem = vscode.window.createStatusBarItem(
        vscode.StatusBarAlignment.Left,
        100
    );
    statusItem.text = '●';
    statusItem.tooltip = 'Codex status';
    statusItem.show();

    const homeDir = process.env.HOME || process.env.USERPROFILE || '';
    const statusFile = path.join(homeDir, '.codex_status');

    const update = () => {
        let val = 'idle';
        try {
            val = fs.readFileSync(statusFile, 'utf8').trim();
        } catch (e) {
            // If file doesn't exist or can't be read, fall back to idle.
        }

        if (val === 'running') {
            statusItem.color = '#00c853'; // green
        } else if (val === 'error') {
            statusItem.color = '#d50000'; // red
        } else {
            statusItem.color = '#9e9e9e'; // grey
        }
    };

    update();

    try {
        fs.watch(statusFile, { persistent: false }, update);
    } catch (e) {
        // If watch fails, we still have the initial state.
    }

    context.subscriptions.push(statusItem);
}

function deactivate() {}

module.exports = { activate, deactivate };

