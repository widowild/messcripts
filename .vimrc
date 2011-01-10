""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Options
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" pour convertir les tab en espaces
set expandtab
" nombre d'espaces par tab
set tabstop=4
" Syntaxique activé:
syntax on
" Theme
set background=dark
" afficher les nombres
set number
" afficher les commandes en cours
set showcmd
" Utilisation de la souris
set mouse=a
" couleur du theme
colorscheme desert
set ai                  " toujours utiliser l'autoindentation
"set backup              " Conserver un fichier de sauvegarde
"activation de l'indentation automatique
set autoindent
set magic               " Enable the "magic"
set ttyfast             " we have a fast terminal
set tw=500              " default textwidth is a max of 5
set undolevels=10000    " 1000 undos
set updatecount=50      " switch every 50 chars
"active les replis
set foldenable
" Avertissement par flash (visual bell) plutôt que par beep
set vb
" Option de la complétion automatique
set wildmode=list:full
" Affiche la paire de parenthèses
set showmatch
" pour convertir les tabs en espaces
set expandtab
" nombre de caractères utilisé pour l'indentation:
set shiftwidth=4
" pour que backspace supprime 4 espaces:
set softtabstop=4
set smartindent

"
" Quickfix
" pour compiler du code python:
" :make <fichier>
set efm=%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m
set makeprg=python

" sur pression de la touche F3, highlight les caractères qui dépassent la 80ème colonne
map <silent> <F3> "<Esc>:match ErrorMsg '\%>80v.\+'<CR>"

" met en surbrillance les espaces et les tabs en trop
" pas réellement pour le python mais j'aime bien
highlight RedundantSpaces ctermbg=red guibg=red
match RedundantSpaces /\s\+$\| \+\ze\t\|\t/

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Plugins
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
autocmd BufReadPost PKGBUILD  set filetype=PKGBUILD
" Turn on omni-completion for the appropriate file types.
autocmd FileType python set omnifunc=pythoncomplete#Complete
autocmd FileType javascript set omnifunc=javascriptcomplete#CompleteJS
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags
autocmd FileType css set omnifunc=csscomplete#CompleteCSS
autocmd FileType xml set omnifunc=xmlcomplete#CompleteTags
autocmd FileType php set omnifunc=phpcomplete#CompletePHP
autocmd FileType c set omnifunc=ccomplete#Complete
autocmd FileType ruby,eruby set omnifunc=rubycomplete#Complete
autocmd FileType ruby,eruby let g:rubycomplete_rails = 1  " Rails support
autocmd FileType java setlocal noexpandtab " don't expand tabs to spaces for Java

" Gérer les fichiers man
runtime plugin/hexman.vim
filetype plugin indent on
source /usr/share/vim/plugin/info.vim
source /usr/share/vim/plugin/hexman.vim
"set runtimepath=~/.vim,$VIM/vimfiles,$VIMRUNTIME,$VIM/vimfiles/after,~/.vim/after
set runtimepath=~/.vim,$VIM/vimfiles,$VIMRUNTIME
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Fonctions
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" fonction qui converti tous les tabs en espaces et met les fichier mac et dos
" au format unix
fun CleanText()
    let curcol = col(".")
    let curline = line(".")
    exe ":retab"
$//ge"xe ":%s/
/ /ge"xe ":%s/
    exe ":%s/ \\+$//e"
    call cursor(curline, curcol)
endfun

if has("autocmd")
  filetype indent on
endif
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Maps
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"Pour exécuter le script python que l'on est en train d'éditer, en appuyant sur la touche F4:
map <silent> <F4> "<Esc>:w!<cr>:!python %<cr>"
" Don't use Ex mode, use Q for formatting
map Q gq
" correction orthographique
map <silent> <F7> "<Esc>:silent setlocal spell! spelllang=fr<CR>"
map <silent> <F8> "<Esc>:silent setlocal spell! spelllang=en<CR>"

imap \date  <C-R>=strftime("%d/%m/%Y")<CR>
