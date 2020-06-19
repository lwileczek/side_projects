imap jk <Esc>
nmap <S-Enter> O<Esc>
nmap <CR> o<Esc>
set textwidth=80
set nocompatible
set ignorecase
set smartcase
set incsearch
set hlsearch
set tabstop=4
set expandtab
set shiftwidth=4
set autoindent
set smartindent
set formatoptions=tcq
syntax on
set spelllang=en
set spellfile=/usr/share/dict/words.utf-8.add  " location may vary, change file to end in <file>.utf-8.add
set ruler
set modeline
set modelines=5
filetype plugin indent on
set dir=~/tmp//  " Where to make tmp files for vim so they don't end up in git repos
" Load all plugins now.
" Plugins need to be added to runtimepath before helptags can be generated.
packloadall
" Load all of the helptags now, after plugins have been loaded.
" All messages and errors will be ignored.
silent! helptags ALL
