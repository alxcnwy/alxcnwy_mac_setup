# Mac Setup


______/\\\_____/\\\\\\\\\\______/\\\\\\\\\\___/\\\\\\\\\\\\\\\_        
 __/\\\\\\\___/\\\///////\\\___/\\\///////\\\_\/////////////\\\_       
  _\/////\\\__\///______/\\\___\///______/\\\_____________/\\\/__      
   _____\/\\\_________/\\\//___________/\\\//____________/\\\/____     
    _____\/\\\________\////\\\_________\////\\\_________/\\\/______    
     _____\/\\\___________\//\\\___________\//\\\______/\\\/________   
      _____\/\\\__/\\\______/\\\___/\\\______/\\\_____/\\\/__________  
       _____\/\\\_\///\\\\\\\\\/___\///\\\\\\\\\/____/\\\/____________ 
        _____\///____\/////////_______\/////////_____\///______________


Everything I need to set up a new mac.

Constantly evolving

Send me feedback / tips on [Twitter @alxcnwy](https://twitter.com/alxcnwy)

# System settings

* Appearance
	* Dark
* Keyboard shortcuts
	* map caps lock -> escape
* Desjtio & Dock
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
* [BetterTouchTool](https://folivora.ai/)
* [Rewind.ai](https://www.rewind.ai/)
* [AutoRaise](https://github.com/sbmpost/AutoRaise/blob/master/AutoRaise.dmg)
* [Bartender](https://www.macbartender.com/)
* [KeyClu](https://github.com/Anze/KeyCluCask/releases/tag/v0.26)
* [XMenu](https://www.devontechnologies.com/apps/freeware)
* [Folder Peek](https://apps.apple.com/us/app/folder-peek/id1615988943?mt=12)
* [little snitch](https://www.obdev.at/products/littlesnitch/download.html)
* [Just focus](https://getjustfocus.com/?ref=just-focus-mac)
* [Monitor control](https://github.com/MonitorControl/MonitorControl)
* [Text sniper](https://textsniper.app/)
* [OmniDiskSweeper](https://www.omnigroup.com/more)
* [itsycal](https://www.mowglii.com/itsycal/datetime.html)
* [istatmenus](https://bjango.com/mac/istatmenus/)
* [HandBrake](https://handbrake.fr/)
* [alt-tab](https://alt-tab-macos.netlify.app/)
* [timingapp](https://timingapp.com)
* [Warp](https://app.warp.dev/)

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

