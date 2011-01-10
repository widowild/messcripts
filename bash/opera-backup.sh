#!/bin/bash 
# Dependance: dialog

#==== Variables ====#

DIALOG=dialog
FOLDEROPERA=/home/$USER/.opera-devel
TMPOPERA=/tmp/opera
DATE=`date -u +%G%m%d`
compteur=10

# Creation du dossier tmp

[ -d "$TMPOPERA" ] || mkdir -p "$TMPOPERA"

if [ -f "/home/$USER/opera-$DATE.tar.xz" ]; then
    $DIALOG --title " Sauvergarde d'opera" --clear \
            --yesno "/home/$USER/opera-$DATE.tar.xz existe
                     Veuillez l'effacer
                     Sauvegarde Annulée" 0 0
case $? in
	0)	exit 0 ;;
	1)	exit 0 ;;
	255)	echo "Appuyé sur Echap. ";;
esac

fi

# Test d'existence du dossier opera:

if [ -d "$FOLDEROPERA" ]; then
    $DIALOG --title " Sauvegarde d'opera" --clear \
            --yesno "Voulez faire un backup?" 0 0

case $? in
	0)	echo "Oui choisi. ";;
	1)	exit 0 ;;
	255)	echo "Appuyé sur Echap. ";;
esac

else
    $DIALOG --title " le dossier $FOLDEROPERA n'existe pas" --clear \
            --yesno "$FOLDEROPERA n'existe pas" 0 0
fi

case $? in
	0)	echo "Oui choisi. ";;
	1)	exit ;;
	255)	echo "Appuyé sur Echap. ";;
esac

BACKUPFOLDER()
{
[ -d "$TMPOPERA/dictionaries" ] || mkdir -p "$TMPOPERA/dictionaries"
[ ! -d "$FOLDEROPERA/dictionaries" ] || cp -R $FOLDEROPERA/dictionaries $TMPOPERA/
echo "Sauvegarde du dossier $FOLDEROPERA/dictionaries"

[ -d "$TMPOPERA/skin" ] || mkdir -p "$TMPOPERA/skin"
[ ! -d "$FOLDEROPERA/skin" ] || cp -R $FOLDEROPERA/skin $TMPOPERA/
echo "Sauvegarde du dossier $FOLDEROPERA/skin"

[ -d "$TMPOPERA/widgets" ] || mkdir -p "$TMPOPERA/widgets"
[ ! -d "$FOLDEROPERA/widgets" ] || cp -R $FOLDEROPERA/widgets $TMPOPERA/
echo "Sauvegarde du dossier $FOLDEROPERA/widgets"

[ -d "$TMPOPERA/UserJS" ] || mkdir -p "$TMPOPERA/UserJS"
[ ! -d "$FOLDEROPERA/UserJS" ] || cp -R $FOLDEROPERA/UserJS $TMPOPERA/
echo "Sauvegarde du dossier $FOLDEROPERA/UserJS"

}

BACKUPFILE()
{
[ ! -f "$FOLDEROPERA/bookmarks.adr" ] || cp $FOLDEROPERA/bookmarks.adr $TMPOPERA/bookmarks.adr
echo "Sauvegarde du fichier $FOLDEROPERA/bookmarks.adr"

[ ! -f "$FOLDEROPERA/bookmarks.ini" ] || cp $FOLDEROPERA/bookmarks.ini $TMPOPERA/bookmarks.ini
echo "Sauvegarde du fichier $FOLDEROPERA/bookmarks.ini"

[ ! -f "$FOLDEROPERA/notes.adr" ] || cp $FOLDEROPERA/notes.adr $TMPOPERA/notes.adr
echo "Sauvegarde du fichier $FOLDEROPERA/notes.adr"

[ ! -f "$FOLDEROPERA/opera6.adr" ] || cp $FOLDEROPERA/opera6.adr $TMPOPERA/opera6.adr
echo "Sauvegarde du fichier $FOLDEROPERA/opera6.adr"

[ ! -f "$FOLDEROPERA/opera6.ini" ] || cp $FOLDEROPERA/opera6.ini $TMPOPERA/opera6.ini
echo "Sauvegarde du fichier $FOLDEROPERA/opera6.ini"

[ ! -f "$FOLDEROPERA/operaprefs.ini" ] || cp $FOLDEROPERA/operaprefs.ini $TMPOPERA/operaprefs.ini
echo "Sauvegarde du fichier $FOLDEROPERA/operaprefs.ini"

[ ! -f "$FOLDEROPERA/opera-newsfeeds.opml" ] || cp $FOLDEROPERA/opera-newsfeeds.opml $TMPOPERA/opera-newsfeeds.opml
echo "Sauvegarde du fichier $FOLDEROPERA/opera-newsfeeds.opml"

[ ! -f "$FOLDEROPERA/pluginpath.ini" ] || cp $FOLDEROPERA/pluginpath.ini $TMPOPERA/pluginpath.ini
echo "Sauvegarde du fichier $FOLDEROPERA/pluginpath.ini"

[ ! -f "$FOLDEROPERA/urlfilter.ini" ] || cp $FOLDEROPERA/urlfilter.ini $TMPOPERA/urlfilter.ini
echo "Sauvegarde du fichier $FOLDEROPERA/urlfilter.ini"

[ ! -f "$FOLDEROPERA/speeddial.ini" ] || cp $FOLDEROPERA/speeddial.ini $TMPOPERA/speeddial.ini
echo "Sauvegarde du fichier $FOLDEROPERA/speeddial.ini"

[ ! -f "$FOLDEROPERA/search.ini" ] || cp $FOLDEROPERA/search.ini $TMPOPERA/search.ini
echo "Sauvegarde du fichier $FOLDEROPERA/search.ini"

[ ! -f "$FOLDEROPERA/unite.adr" ] || cp $FOLDEROPERA/unite.adr $TMPOPERA/unite.adr
echo "Sauvegarde du fichier $FOLDEROPERA/unite.adr"

[ ! -f "$FOLDEROPERA/wand.dat" ] || cp $FOLDEROPERA/wand.dat $TMPOPERA/wand.dat
echo "Sauvegarde du fichier $FOLDEROPERA/wand.dat"

# Compte Mail:
[ -d "$TMPOPERA/mail" ] || mkdir -p "$TMPOPERA/mail"
[ ! -f "$FOLDEROPERA/mail/accounts.ini" ] || cp $FOLDEROPERA/mail/accounts.ini $TMPOPERA/mail/accounts.ini
echo "Sauvegarde du fichier $FOLDEROPERA/mail/accounts.ini"

[ -d "$TMPOPERA/mail/autofilter" ] || mkdir -p "$TMPOPERA/mail/autofilter"
[ ! -f "$FOLDEROPERA/mail/autofilter/filter_8.ini" ] || cp $FOLDEROPERA/mail/autofilter/filter_8.ini $TMPOPERA/mail/autofilter/filter_8.ini
echo "Sauvegarde du fichier $FOLDEROPERA/autofilter/filter_8.ini"


[ ! -f "$FOLDEROPERA/contacts.adr" ] || cp $FOLDEROPERA/contacts.adr $TMPOPERA/contacts.adr
echo "Sauvegarde du fichier $FOLDEROPERA/contacts.adr"

# Compte Unite

[ ! -f "$FOLDEROPERA/unite.adr" ] || cp $FOLDEROPERA/unite.adr $TMPOPERA/unite.adr
echo "Sauvegarde du fichier $FOLDEROPERA/unite.adr"
}

COMPRESSEUR() {
if [ -f /home/$USER/opera-$DATE.tar.xz ];then
    echo "/home/$USER/opera-$DATE.tar.xz existe"
else
    cd $TMPOPERA
    bsdtar cJf /home/$USER/opera-$DATE.tar.xz ./
fi
}

#==== Barre d'avancement ====#
(
while test $compteur != 110
do
echo $compteur
BACKUPFOLDER
BACKUPFILE
COMPRESSEUR
echo "Le nouveau\n\message ($compteur pourcent)"
echo "XXX"
compteur=`expr $compteur + 10`
sleep 1
done
) |
$DIALOG --title "Sauvegarde d'opera" --gauge "Traitement en cours..." 20 70 0
