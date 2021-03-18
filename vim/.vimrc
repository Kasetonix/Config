" Vim plug
call plug#begin('~/.vim/plugged')
Plug 'morhetz/gruvbox' " Gruvbox theme
Plug 'arcticicestudio/nord-vim' " Nord theme
Plug 'vim-airline/vim-airline' " Vim airline
Plug 'vim-airline/vim-airline-themes' " Themes for vim airline
Plug 'chiel92/vim-autoformat' " Autoformatting
Plug 'hdima/python-syntax' " Python syntax highligting
call plug#end()

" Editor settings
set number " Setting line numbers
set relativenumber " setting relative line numbers
set tabstop=2 " Setting tab length
set expandtab " Changing tabs to spaces
set softtabstop=2 " Deleting multiple spaces in the row
set encoding=utf-8 " Setting encoding
set wrap " Wrapping text if it goes beyond screen width
syntax on " Enabling syntax highlighting

" Theming
colorscheme gruvbox " Setting Gruvbox theme
set bg=dark " Setting dark background
hi Normal guibg=NONE ctermbg=NONE " Enabling transparency
set noshowmode " Removing bottom bar
 
