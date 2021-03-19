# Dotfiles
This repo contains most of my own dotfiles files - most important ones.

# Alacritty Install
**Install**

Dependencies: 

`sudo apt-get install cmake pkg-config libfreetype6-dev libfontconfig1-dev libxcb-xfixes0-dev python3`

Cloning the source code:

`git clone https://github.com/alacritty/alacritty.git`

`cd alacritty`

Building:

`cd alacritty`

`cargo build --release`

# Fonts
You just have to place fonts in ~/.fonts folder (you may have to create it).

# i3 Install

**Base i3 install**

**Ubuntu Repostitory**

`sudo /usr/lib/apt/apt-helper download-file https://debian.sur5r.net/i3/pool/main/s/sur5r-keyring/sur5r-keyring_2021.02.02_all.deb keyring.deb SHA256:cccfb1dd7d6b1b6a137bb96ea5b5eef18a0a4a6df1d6c0c37832025d2edaa710`

`sudo dpkg -i ./keyring.deb`

`echo "deb http://debian.sur5r.net/i3/ $(grep '^DISTRIB_CODENAME=' /etc/lsb-release | cut -f2 -d=) universe" >> /etc/apt/sources.list.d/sur5r-i3.list`

`sudo apt-get update`

`sudo apt-get install i3`

**i3-gaps install**
i3-gaps is a fork giving you option to have gaps around windows, which I use in my config



