#export LC_ALL=en_US.UTF-8
#export LC_CTYPE=en_US.UTF-8

# Check for an interactive session
[ -z "$PS1" ] && return
alias nrjHit='mplayer mms://vipnrj.yacast.net/nrj_tvhit'
alias ls='ls --color'
alias cdl="cd $1 | ls"
#PS1='[\u@\h \W]\$ '
#PS1='[\u@\h \W] Utilise \$\033[1;31m '

# Doc Python
export PYTHONDOCS=/usr/share/doc/python/html/

# Wine
alias wine32="sh ~/.script/wine32.sh"
alias wine64="sh ~/.script/wine64.sh"
# affichage sympathique de la ligne de commande
PS1="[\t] \[\e[01;32m\]\u@\h\[\e[00m\]:\[\e[01;34m\]\w\[\e[00m\]\$ "

halt(){
#à ajouter dans le $HOME/.bashrc
notify-send -t 1000 -u critical "ATTENTION vous lancez la commande "halt""
}

boinccompilation() {
cd /media/HDD120/archlinux/boinc-svn/
makepkg
}
bleachbitcompilation() {
cd /media/HDD120/archlinux/bleachbit-svn/
makepkg
}

xonoticcompilation() {
cd /media/HDD120/archlinux/xonotic-git/
makepkg
}
clamavcompilation() {
cd /media/HDD120/archlinux/clamav-git/
makepkg
}

clamhome() {
clamscan --bell -r -i --log=/tmp/virus.log ~/
}

mirror() {
cd /media/TERATOR/mirror/scripts/
sh ./repomirror.sh
}

mybook() {
rsync -e ssh -avz --delete-after /media/TERATOR/mirror/ root@192.168.0.10:/shares/mirror/
}

wallpaper() {
cd /media/TERATOR/
wget --mirror http://images.alphacoders.com
}

allcompilation() {
boinccompilation && clamavcompilation && xonoticcompilation && bleachbitcompilation 

}

widoclean() {
sh /media/HDD120/pkg/widoclean.sh
}

ftpsexy() {
wget -c "ftp://87.224.173.61/_XXX/B/Brandi%20Belle%206%20%20%CA%F0%E0%F1%E0%E2%E8%F6%E0%20%C1%F0%E5%ED%E4%E8%206%20(DVDRip)/brandib6.avi"
}

# Paramètre réseau pour mpd
export MPD_HOST="127.0.0.1"
export MPD_PORT="6600"

# editeur de texte par défaut:
EDITOR="gvim"
VISUAL=$EDITOR
export EDITOR VISUAL

export HISTSIZE=10000 # taille de l'historique 
export HISTFILESIZE=${HISTSIZE}
export HISTIGNORE="ls:cd:[bf]g:exit" # ignorer les lignes w/ ls, cd, ...
export HISTCONTROL="ignoreboth" # ignorer les doublons et les commandes qui commencent par un espace

# fond d'écran
#eval `cat ~/.fehbg` &

# Interdire l'écrasement de fichier avec >
set -C

shopt -s cdspell # Pour que bash corrige automatiquement les fautes de frappes ex: cd ~/fiml sera remplacé par cd ~/film
shopt -s checkwinsize # Pour que bash vérifie la taille de la fenêtre après chaque commande
shopt -s cmdhist # Pour que bash sauve dans l'historique les commandes qui prennent plusieurs lignes sur une seule ligne.
shopt -s dotglob # Pour que bash montre les fichiers qui commencent par un .
shopt -s expand_aliases # # Pour que bash montre la commande complete au lieu de l'alias
shopt -s extglob # Pour que bash, interprète les expressions génériques
shopt -s histappend # Pour que bash ajoute au lieu d'écraser dans l'histo
shopt -s hostcomplete # Pour que bash tente de résoudre le nom pour les ip suivis d'un @
shopt -s nocaseglob # Pour que bash ne soit pas sensible a la casse
