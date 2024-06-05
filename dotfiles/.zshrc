export AWS_ACCESS_KEY_ID='xx'
export AWS_SECRET_ACCESS_KEY='xx'

alias ssh-production='gcloud compute ssh --zone "europe-west3-c" "tst-production"  --project "aisupervision-tst"'
alias ssh-staging='gcloud compute ssh --zone "europe-west3-c" "tst-staging"  --project "aisupervision-tst"'
alias ssh-numberboost='gcloud compute ssh --zone "us-central1-a" "numberboost-prod"  
--project "numberboost"'

export EDITOR=nano
export VISUAL="$EDITOR"
 
export PATH="/opt/homebrew/bin:$PATH"
export PATH="/usr/local/bin:/usr/bin:/bin:$PATH"
export PATH="$HOME/anaconda3/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:$PATH"

#export CLOUDSDK_PYTHON=python2

POWERLEVEL9K_VIRTUALENV_BACKGROUND=10

# sublime text
alias subl="'/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl'"

# mysql
#export PATH=/usr/local/Cellar/mysql/8.0.21_1/bin:$PATH
export PATH=$PATH:/usr/local/mysql/bin


# fix zsh-syntax-highlighting-slow-paste
pasteinit() {
  OLD_SELF_INSERT=${${(s.:.)widgets[self-insert]}[2,3]}
  zle -N self-insert url-quote-magic # I wonder if you'd need `.url-quote-magic`?
}

pastefinish() {
  zle -N self-insert $OLD_SELF_INSERT
}
zstyle :bracketed-paste-magic paste-init pasteinit
zstyle :bracketed-paste-magic paste-finish pastefinish


# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/Users/alexc/.oh-my-zsh"

# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
# zsh theme
ZSH_THEME="powerlevel9k/powerlevel9k"
#POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(time)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status virtualenv)
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir)

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(virtualenv git zsh-autosuggestions autojump)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
alias ju="jupyter notebook"
alias la="ls -la"
alias py="python"

source /Users/alexc/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

export PYENV_ROOT="$HOME/.pyenv"
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"




# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/alexc/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/alexc/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/alexc/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/alexc/google-cloud-sdk/completion.zsh.inc'; fi

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/alexc/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/alexc/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/alexc/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/alexc/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

