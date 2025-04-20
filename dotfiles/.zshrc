# Aliases
alias concat="python3 /Users/alexc/Documents/_____setup/alxcnwy_mac_setup/scripts/concat.py"
alias ju="jupyter notebook"
alias la="ls -la"
alias py="python"

# sublime text
alias subl="'/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl'"

# AWS credentials
export AWS_ACCESS_KEY_ID='xx'
export AWS_SECRET_ACCESS_KEY='xx'

# Preferred editor
export EDITOR=nano
export VISUAL="$EDITOR"

# Path config
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/Users/alexc/anaconda3/bin:$PATH"
export PATH=$PATH:/usr/local/mysql/bin

# Oh My Zsh
export ZSH="/Users/alexc/.oh-my-zsh"
ZSH_THEME="powerlevel9k/powerlevel9k"
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status virtualenv)
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir)

plugins=(virtualenv git zsh-autosuggestions autojump)
source $ZSH/oh-my-zsh.sh

# Fix zsh-syntax-highlighting slow paste
pasteinit() {
  OLD_SELF_INSERT=${${(s.:.)widgets[self-insert]}[2,3]}
  zle -N self-insert url-quote-magic
}
pastefinish() {
  zle -N self-insert $OLD_SELF_INSERT
}
zstyle :bracketed-paste-magic paste-init pasteinit
zstyle :bracketed-paste-magic paste-finish pastefinish

# zsh-syntax-highlighting
source /Users/alexc/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Pyenv
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Google Cloud SDK
if [ -f '/Users/alexc/google-cloud-sdk/path.zsh.inc' ]; then
  . '/Users/alexc/google-cloud-sdk/path.zsh.inc'
fi
if [ -f '/Users/alexc/google-cloud-sdk/completion.zsh.inc' ]; then
  . '/Users/alexc/google-cloud-sdk/completion.zsh.inc'
fi

# Conda init
# !! Contents managed by 'conda init' !!
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
