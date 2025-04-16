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

Send me feedback / tips on [Twitter @alxcnwy](https://twitter.com/alxcnwy)

GLHF

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
* [Bartender](https://www.macbartender.com/)
* [BetterTouchTool](https://folivora.ai/) (paid - def worth it)
* [Folder Peek](https://apps.apple.com/us/app/folder-peek/id1615988943?mt=12)
* [HandBrake](https://handbrake.fr/)
* [Hazel](https://www.noodlesoft.com/)
* [istatmenus](https://bjango.com/mac/istatmenus/)
* [KeyClu](https://github.com/Anze/KeyCluCask/releases/tag/v0.26)
* [little snitch](https://www.obdev.at/products/littlesnitch/download.html) (paid - def worth it)
* [Monitor control](https://github.com/MonitorControl/MonitorControl)
* [Rewind.ai](https://www.rewind.ai/)
* [Rocket](https://matthewpalmer.net/rocket/) (get pro, def worth it)
* [Text sniper](https://textsniper.app/) (paid)
* [timingapp](https://timingapp.com)
* [Warp](https://app.warp.dev/)
* [XMenu](https://www.devontechnologies.com/apps/freeware)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)

# Terminal

Install Warp.

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

# Remember
It's impossible to break your computer. If something goes wrong, just reset and restore backup! 