# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Zinit home directory 
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"

# Installing Zinit If not installed
[ ! -d $ZINIT_HOME ] && mkdir -p "$(dirname $ZINIT_HOME)"
[ ! -d $ZINIT_HOME/.git ] && git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"

# Loading Zinit
source "${ZINIT_HOME}/zinit.zsh"

# Add powerlevel10k 
zinit ice depth=1; zinit light romkatv/powerlevel10k

# Add other zsh plugins
# zinit ice wait lucid
zinit light zsh-users/zsh-syntax-highlighting
# zinit ice wait lucid
zinit light zsh-users/zsh-completions
# zinit ice wait lucid
zinit light zsh-users/zsh-autosuggestions
# zinit ice wait lucid
zinit light Aloxaf/fzf-tab

# Keybindings
bindkey -e
bindkey '^[[3~' delete-char
bindkey '^b' backward-word 
bindkey '^w' forward-word
bindkey '^d' delete-word
bindkey '^j' up-line-or-history
bindkey '^k' down-line-or-history

# History
HISTSIZE=5000
HISTFILE=~/.zsh_history
SAVEHIST=$HISTSIZE
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups

# Completion styling (removing case-sensitivenesss)
zstyle ":completion:*" matcher-list 'm:{a-z}={A-Za-z}'
zstyle ":completion:*" list-colors "${(s.:.)LS_COLORS}"
zstyle ":completion:*" menu no
zstyle ":fzf-tab:complete:cd:*" fzf-preview 'ls --color $realpath'
zstyle ":fzf-tab:complete:__zoxide_z:*" fzf-preview 'ls --color $realpath'


# Load completions
autoload -U compinit && compinit


# Zsh Options
ENABLE_CORRECTION="true"
COMPLETION_WAITING_DOTS="%F{blue}...%f"
DISABLE_UNTRACKED_FILES_DIRTY="true"
unsetopt BEEP


# Aliases
alias n="nvim"
alias ncmpcpp="ncmpcpp -p 6200"
alias getMusic="python $HOME/scripts/getMusic.py"
alias i="sudo pacman -S "
alias iAur="paru -S"
alias s="pacman -Ss "
alias sAur="paru -Ss "
alias up="paru -Syu"
alias cd="z"
alias cdd="cd"
alias rAudio="systemctl --user restart wireplumber pipewire-pulse pipewire"
alias rInternet="sudo systemctl restart NetworkManager"
alias ls="eza -a --icons=always"
alias rel="xrdb merge ~/.Xresources"
alias noanim="pkill picom"

# Shell integrations 
eval "$(fzf --zsh)"
eval "$(zoxide init zsh)"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
export PATH="$PATH:/home/shibam/.modular/bin"
