# Mac Setup

Everything I need to set up a new mac.

Constantly evolving

https://twitter.com/alxcnwy

# Apps
Install the apps in `mac_apps.txt` - most are from the app store but specialist ones below:
* [BetterTouchTool](https://folivora.ai/)
* [Rewind.ai](https://www.rewind.ai/)
* [little snitch](https://www.obdev.at/products/littlesnitch/download.html)
* [Just focus](https://getjustfocus.com/?ref=just-focus-mac)
* [Monitor control](https://github.com/MonitorControl/MonitorControl)
* [Text sniper](https://textsniper.app/)

# Terminal
## setup iterm
[ref](https://www.freecodecamp.org/news/how-to-configure-your-macos-terminal-with-zsh-like-a-pro-c0ab3f3c1156/)

load saved preference file

## setup oh-my-zsh

` git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`

copy `dotfiles/.zshrc` into `~`

[install shell integrations](https://itectec.com/superuser/macos-copy-the-output-of-the-last-command-in-iterm2/) to enable copy last output shortcut (cmd+shift+a)

## setup autojump
[ref](https://github.com/wting/autojump)

## setup homebrew

### save
`brew list | xargs -L1 > Brewfile`

### load
`cat Brewfile | xargs brew`

## setup sublime
[ref](https://webdesign.tutsplus.com/articles/simple-visual-enhancements-for-better-coding-in-sublime-text--webdesign-18052)


# System settings

Todo

* Keyboard shortcuts
* Dock preferences
* Trackpad settings
* Notifications
* Energy Saver
* Security and Privacy
* Sharing and Bluetooth