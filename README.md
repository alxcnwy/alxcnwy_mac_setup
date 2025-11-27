# Mac Setup

```
______/\\\_____/\\\\\\\\\\______/\\\\\\\\\\___/\\\\\\\\\\\\\\\_        
 __/\\\\\\\___/\\\///////\\\___/\\\///////\\\_\/////////////\\\_       
  _\/////\\\__\///______/\\\___\///______/\\\_____________/\\\/__      
   _____\/\\\_________/\\\//___________/\\\//____________/\\\/____     
    _____\/\\\________\////\\\_________\////\\\_________/\\\/______    
     _____\/\\\___________\//\\\___________\//\\\______/\\\/________   
      _____\/\\\__/\\\______/\\\___/\\\______/\\\_____/\\\/__________  
       _____\/\\\_\///\\\\\\\\\/___\///\\\\\\\\\/____/\\\/____________ 
        _____\///____\/////////_______\/////////_____\///______________
```

Everything I need to set up a new mac.

Constantly evolving

Send me feedback / tips on [Twitter @alxcnwy](https://twitter.com/alxcnwy) or [LinkedIn](https://www.linkedin.com/in/alxcnwy/)

I build cool AI stuff and do consulting: [NumberBoost.com](https://www.numberboost.com)

GLHF 🫡

# Mac System settings

* Appearance
	* Dark
* Keyboard shortcuts
	* map caps lock -> escape
* Desktop & Dock
	* setup hot corners
		* top left: Put Display to Sleep
		* top right: Mission Control
		* bottom left: Start Screen Saver
		* bottom right: Desktop
* Screensaver
	* Setup Matrix screensaver in this repo
	* Set screen lock to 60 seconds
* Trackpad settings
	* max out trackpad speed
	* turn on tap to click
	* change swipe between pages to two fingers
	* change swipe between full screen apps to four fingers
	* change mission control to swipe up four fingers
* Energy Saver
* Security and Privacy
	* turn on FileVault
	* audit location and other permissions

# Apps
Install the apps in `mac_apps.txt` - most are from the app store but specialist ones below:
* [alt-tab](https://alt-tab-macos.netlify.app/)
* [Arq Backup](https://www.arqbackup.com/)
* [Bartender](https://www.macbartender.com/)
* [BetterTouchTool](https://folivora.ai/) (paid - def worth it)
* [Horo timer](https://matthewpalmer.net/horo-free-timer-mac/)
* [KeyClu](https://github.com/Anze/KeyCluCask/releases/tag/v0.26)
* [little snitch](https://www.obdev.at/products/littlesnitch/download.html) (paid - def worth it)
* [Monitor control](https://github.com/MonitorControl/MonitorControl)
* [Rewind.ai](https://www.rewind.ai/)
* [Rocket](https://matthewpalmer.net/rocket/) (get pro, def worth it)
* [Text sniper](https://textsniper.app/) (paid)
* [Ghostty](https://ghostty.org/)
* [XMenu](https://www.devontechnologies.com/apps/freeware)
* [Visual Studio Code](https://code.visualstudio.com/) — see `vscode/README.md` for config and `vscode/KEYBINDINGS.md` for keyboard shortcuts.

## Config symlinks per Mac (VS Code + BetterTouchTool)

These live outside the repo, so you must re-create the symlinks once on every new Mac after cloning this repo.

### VS Code user settings

VS Code stores user config in `~/Library/Application Support/Code/User`. To make this repo the source of truth:

```bash
CODE_USER="$HOME/Library/Application Support/Code/User"

# Optional: back up any existing files first
mv "$CODE_USER/keybindings.json" "$CODE_USER/keybindings.json.backup" 2>/dev/null || true
mv "$CODE_USER/settings.json" "$CODE_USER/settings.json.backup" 2>/dev/null || true

ln -s "$HOME/Documents/_____setup/alxcnwy_mac_setup/vscode/keybindings.json" "$CODE_USER/keybindings.json"
ln -s "$HOME/Documents/_____setup/alxcnwy_mac_setup/vscode/settings.json" "$CODE_USER/settings.json"
```

Run those once per machine; afterwards, editing the repo files updates VS Code.

### BetterTouchTool config

BetterTouchTool stores its config under `~/Library/Application Support/BetterTouchTool`.

- To take a one-off snapshot into the repo (safe default):

  ```bash
  cd "$HOME/Documents/_____setup/alxcnwy_mac_setup"
  python3 scripts/sync_bettertouchtool.py
  ```

  This writes a copy to `app_config_files/bettertouchtool/live`.

- To make the repo the live config location (symlinked):

  1. Quit BetterTouchTool completely.
  2. Run:

     ```bash
     cd "$HOME/Documents/_____setup/alxcnwy_mac_setup"
     python3 scripts/sync_bettertouchtool.py --link --force
     ```

  This moves the BetterTouchTool config into `app_config_files/bettertouchtool/live` and replaces the original folder with a symlink. You need to do this once per Mac.

# Terminal

## setup oh-my-zsh

` git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`

copy `dotfiles/.zshrc` into `~`

[install shell integrations](https://itectec.com/superuser/macos-copy-the-output-of-the-last-command-in-iterm2/) to enable copy last output shortcut (cmd+shift+a)

## setup autojump
[ref](https://github.com/wting/autojump)

## setup magic-dashboard
[ref](https://github.com/chrisgrieser/zsh-magic-dashboard)

## setup homebrew

### save
`brew list | xargs -L1 > Brewfile`

### load
`cat Brewfile | xargs brew`

## project bootstrap script

There is a simple per-project bootstrap helper in `scripts/bootstrap` that:

* creates a `.venv` in the current directory
* upgrades `pip`/`wheel` and installs `flask`
* copies this repo's `AGENTS.md` into the project as `AGENTS.md` (overwriting if present)
* creates simple `spec.md`, `todo.md`, and `README.md` templates (if missing)

### What it sets up

When you run `scripts/bootstrap` inside a project folder, you get:

* `AGENTS.md` — the source of truth for how AI assistants (Codex CLI, etc.) should behave in that repo. It includes rules like “do not overengineer”, how to use the markdown files, and a simple Git/GitHub workflow.
* `spec.md` — a one-page project spec: what you’re building, who it’s for, and the MVP scope. This is intentionally lightweight; it’s not a long PRD.
* `todo.md` — a small, focused task list. Use it to track the next few things to ship; prune it instead of adding process.
* `README.md` — a minimal “how to run this” doc with a Getting Started section (activate `.venv`, run `flask`, etc.).

The goal is to make it fast to start a new project with:

* a working Python/Flask environment
* a clear, simple way to run the app
* just enough structure to capture intent and next steps
* strong defaults that remind you not to overengineer

### Recommended new-project flow

1. Create a new folder for your project and `cd` into it.
2. Run the bootstrap script:

   ```bash
   /Users/alexc/Documents/_____setup/alxcnwy_mac_setup/scripts/bootstrap
   ```

   (or use the `bootstrap` shell alias below).

3. Open `README.md` and adjust the Getting Started commands if needed.
4. Fill in `spec.md` with a one-sentence summary, who it’s for, and 2–3 MVP bullets.
5. Add a few concrete items to `todo.md` (ideally tasks you can do today).
6. Skim `AGENTS.md` so your AI assistant follows your preferences in that repo.

### Optional global alias (run once in a shell)

```bash
cd /Users/alexc/Documents/_____setup/alxcnwy_mac_setup
echo 'alias bootstrap="'$(pwd)'/scripts/bootstrap"' >> ~/.zshrc
source ~/.zshrc
```

## ChatGPT / Codex history backup

Use `scripts/backup_chatgpt.py` to export Codex CLI session history (`~/.codex/sessions`) into flat text files under `~/Documents/_____db/chatgpt`.

From this repo:

```bash
cd /Users/alexc/Documents/_____setup/alxcnwy_mac_setup
python3 scripts/backup_chatgpt.py
```

Each run will create timestamped files like `YYYY-MM-DD_HH-MM-SS__SESSIONID.txt` containing the events for each session.

# Parting advice
It's impossible to break your computer. 

If something goes wrong, just reset and restore backup! 

And always have at least 2 backups - 1 physical, 1 online. 

Godspeed 🫡


```
brew install --cask qlcolorcode qlstephen qlmarkdown
qlmanage -r
qlmanage -r cache
```
