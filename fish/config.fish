########
# PATH #
########
  export PATH="$HOME/.apps/:$PATH"
  export PATH="$HOME/.emacs.d/bin:$PATH"
  export PATH="$HOME/.apps/spicetify-cli:$PATH"
  export PATH="$HOME/.apps/pico-8:$PATH"
  export PATH="$HOME/.cargo/bin/:$PATH"

#####################
# Variable Settings #
#####################
  set EDITOR "vim"

###########
# Aliases #
###########
  alias ll='ls -Alh'
  alias la='ls -Ah'
  alias lh='ls --format=single-column'
  alias ..='cd ..'
  alias df='df -h'
  alias matrix='cmatrix -a -B -s'
  alias matrix-blue='cmatrix -a -B -s -C blue'
  alias speedtest='speedtest-cli --bytes --single'
  alias synaptic='sudo synaptic'
  alias c='clear'
  alias cls='clear'
  alias conf-i3='vim ~/.config/i3/config'
  alias conf-openbox='cd ~/.config/openbox'
  alias conf-alacritty='vim ~/.config/alacritty/alacritty.yml'
  alias conf-polybar='vim ~/.config/polybar/config'
  alias conf-bash='vim ~/.bashrc'
  alias conf-vim='vim ~/.vimrc'
  alias conf-qutebrowser='vim ~/.config/qutebrowser/config.py'
  alias conf-spicetify='cd ~/.config/spicetify'
  alias conf-fish='vim ~/.config/fish/config.fish'
  alias Coding='cd ~/Documents/Coding'
  alias clock='tty-clock'
  alias minecraft-screens='cp ~/.minecraft/screenshots/* ~/Pictures/ScreenShots/Other'
  alias empty-trash='rm -r ~/Trashcan/*'
  alias emacs-term="emacs -nw"
  alias fetch="neofetch"
  alias Git="cd ~/Documents/Git"
  alias name="echo $USER/$HOSTNAME"
  alias vimtutorshort="vim ~/Documents/VIMTutorSummaries.txt"
  alias Print="figlet -f ansi-shadow.flf -d /usr/share/figlet/"
  alias SchoolHTML="cd ~/Documents/Coding/HTML/School"

#############
# Functions #
#############
  function Update
  	clear
    echo
  	echo "*** System update initialized ***"
  	echo
  	echo "Enter root password..."
  	sudo apt-get update -y
    sudo apt-get upgrade -y
  	echo
  	echo "*** System is up-to-date! ***"
    echo
  end

#############
# Autostart #
#############
  /home/kasetonix/Documents/Coding/Shell/fish.sh
  echo 

