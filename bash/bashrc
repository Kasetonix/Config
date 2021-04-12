# ██████╗  █████╗ ███████╗██╗  ██╗██████╗  ██████╗
# ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗██╔════╝
# ██████╔╝███████║███████╗███████║██████╔╝██║
# ██╔══██╗██╔══██║╚════██║██╔══██║██╔══██╗██║
# ██████╔╝██║  ██║███████║██║  ██║██║  ██║╚██████╗
# ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝

# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# Exporting /bin to PATH
export PATH="/bin:/usr/bin:$PATH" 

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac
# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

# Defaults
# if [ "$color_prompt" = yes ]; then
#     PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
# else
#     PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
# fi

# Custom
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\w \[\[\033[00;36m\]❯\[\033[00m\] '
else
    PS1='${debian_chroot:+($debian_chroot)}\w:$ '
fi


unset color_prompt force_color_prompt

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).

#######################
### Custom Commands ###
#######################

  ########
  # PATH #
  ########
    export PATH="$HOME/.apps/:$PATH"
    export PATH="$HOME/.emacs.d/bin:$PATH"
    export PATH="$HOME/.apps/spicetify-cli:$PATH"
    export PATH="$HOME/.apps/pico-8:$PATH"
    export PATH="$HOME/.apps/voxatron:$PATH"
    export PATH="$HOME/.cargo/bin/:$PATH"

  #####################
  # Variable Settings #
  #####################
    set EDITOR "vim"

  ###########
  # Aliases #
  ###########
    alias ls="dir --color"
    alias ll='ls -Alh'
    alias la='ls -Ah'
    alias lh='ls --format=single-column'
    alias dir="dir --color"
    alias ..='cd ..'
    alias df='df -h'
    alias matrix='cmatrix -a -B -s'
    alias matrix-blue='cmatrix -a -B -s -C blue'
    alias speedtest='speedtest-cli --bytes --single'
    alias synaptic='sudo synaptic'
    alias c='clear'
    alias cls='clear'
    alias untar="tar -xf"
    alias conf-i3='vim ~/.config/i3/config'
    alias conf-openbox='cd ~/.config/openbox'
    alias conf-alacritty='vim ~/.config/alacritty/alacritty.yml'
    alias conf-polybar='vim ~/.config/polybar/config'
    alias conf-bash='vim ~/.bashrc'
    alias conf-vim='vim ~/.vimrc'
    alias conf-qutebrowser='vim ~/.config/qutebrowser/config.py'
    alias conf-spicetify='cd ~/.config/spicetify'
    alias conf-fish='vim ~/.config/fish/config.fish'
    alias conf-neofetch='vim ~/.config/neofetch/config.conf'
    alias conf-amfora="vim ~/.config/amfora/config.toml"
    alias conf-zathura="vim ~/.config/zathura/zathurarc"
    alias Coding='cd ~/Documents/Coding'
    alias clock='tty-clock'
    alias minecraft-screens='cp ~/.minecraft/screenshots/* ~/Pictures/ScreenShots/Other'
    alias emacs-term="emacs -nw"
    alias fetch="neofetch"
    alias neofetch-small="neofetch --ascii_distro Pop_OS_small --disable title underline model packages shell wm_theme font term cpu gpu memory users --block_range 0 7" 
    alias fetch-small="neofetch-small"
    alias logo="neofetch -L --ascii_distro $1"
    alias logo-clear='clear && neofetch -L --ascii_distro $1'
    alias logo-small="neofetch -L --ascii_distro $1_small"
    alias Git="cd ~/Documents/Git"
    alias name="echo $USER/$HOSTNAME"
    alias vimtutorshort="vim ~/Documents/VIMTutorSummaries.txt"
    alias Print="figlet -f ansi-shadow.flf -d /usr/share/figlet/"
    alias SchoolHTML="cd ~/Documents/Coding/HTML/School"
    alias dwm-make="cd ~/.config/dwm/ && sudo make install && cd -"
    alias Notes="cd ~/Documents/Notes"

  #############
  # Autostart #
  #############
    neofetch-small
    LC_ALL="en_US.UTF-8"
    LANG="en_US.UTF-8"
    LANGUAGE="en_US:en"
    # /home/kasetonix/Documents/Coding/Shell/bash.sh
    # echo 

  #################
  ### Functions ###
  #################
  Update () {
  	clear
        echo
  	echo "*** System update initialized ***"
  	echo
  	echo "Enter admin password..."
  	sudo apt-get update -y
  	sudo apt-get dist-upgrade -y
        sudo apt-get upgrade -y
  	sudo apt-get update -y
  	echo
  	echo "*** System updated succsesfully! ***"
    echo
  } 
  
  export Update


  ###########################  
  ### Colorful less pages ###
  ###########################
    export LESS="-R"
    export LESS_TERMCAP_mb=$(printf '\e[01;32m')        # enter blinking            mode
    export LESS_TERMCAP_md=$(printf '\e[01;34;5;75m')   # enter double-bright       mode
    export LESS_TERMCAP_me=$(printf '\e[0m')            # turn off all appearance   modes (mb, md, so, us)
    export LESS_TERMCAP_so=$(printf '\e[01;36m')        # enter standout            mode
    export LESS_TERMCAP_se=$(printf '\e[0m')            # leave standout            mode
    export LESS_TERMCAP_us=$(printf '\e[04;33;5;200m')  # enter underline           mode
    export LESS_TERMCAP_ue=$(printf '\e[0m')            # leave underline
