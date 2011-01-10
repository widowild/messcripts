#!/bin/bash
# Dependance: dialog

#==== Variables ====#

DIALOG=dialog
FOLDERPIDGIN=/home/$USER/.purple
TMPPIDGIN=/tmp/.purple
DATE=`date -u +%G%m%d`
compteur=10

# Creation du dossier tmp

cleanfile() {
    $DIALOG --title " pidgin-$DATE.tar.xz " --clear \
            --yesno "supprimer /home/$USER/pidgin-$DATE.tar.xz ?" 0 0
case $? in
	0)	rm /home/$USER/pidgin-$DATE.tar.xz ;;
	1)	exit 0 ;;
	255)	echo "Appuyé sur Echap. ";;
esac
}


[ -d "$TMPPIDGIN" ] || mkdir -p "$TMPPIDGIN"

if [ -f "/home/$USER/pidgin-$DATE.tar.xz" ]; then
    $DIALOG --title " Sauvergarde de pidgin " --clear \
            --yesno "/home/$USER/pidgin-$DATE.tar.xz existe
                     Veuillez l'effacer" 0 0
case $? in
	0)	exit 0 ;;
	1)	cleanfile ;;
	255)	echo "Appuyé sur Echap. ";;
esac

fi

# Test d'existence du dossier pidgin:

if [ -d "$FOLDERPIDGIN" ]; then
    $DIALOG --title " Sauvegarde de pidgin" --clear \
            --yesno "Voulez faire un backup?" 0 0

case $? in
	0)	echo "Oui choisi. ";;
	1)	exit 0 ;;
	255)	echo "Appuyé sur Echap. ";;
esac

else
    $DIALOG --title " le dossier $FOLDERPIDGIN n'existe pas" --clear \
            --yesno "$FOLDERPIDGIN n'existe pas" 0 0
fi

case $? in
	0)	echo "Oui choisi. ";;
	1)	exit ;;
	255)	echo "Appuyé sur Echap. ";;
esac

BACKUPFOLDER()
{
[ -d "$TMPPIDGIN/certificates" ] || mkdir -p "$TMPPIDGIN/certificates"
[ ! -d "$FOLDERPIDGIN/certificates" ] || cp -R $FOLDERPIDGIN/certificates $TMPPIDGIN/certificates
echo "Sauvegarde du dossier $FOLDERPIDGIN/certificates"

[ -d "$TMPPIDGIN/custom_smiley" ] || mkdir -p "$TMPPIDGIN/custom_smiley"
[ ! -d "$FOLDERPIDGIN/custom_smiley" ] || cp -R $FOLDERPIDGIN/custom_smiley $TMPPIDGIN/custom_smiley
echo "Sauvegarde du dossier $FOLDERPIDGIN/custom_smiley"

[ -d "$TMPPIDGIN/icons" ] || mkdir -p "$TMPPIDGIN/icons"
[ ! -d "$FOLDERPIDGIN/icons" ] || cp -R $FOLDERPIDGIN/icons $TMPPIDGIN/icons
echo "Sauvegarde du dossier $FOLDERPIDGIN/icons"

[ -d "$TMPPIDGIN/logs" ] || mkdir -p "$TMPPIDGIN/logs"
[ ! -d "$FOLDERPIDGIN/logs" ] || cp -R $FOLDERPIDGIN/logs $TMPPIDGIN/logs
echo "Sauvegarde du dossier $FOLDERPIDGIN/logs"
}

BACKUPFILE()
{
[ ! -f "$FOLDERPIDGIN/accels" ] || cp $FOLDERPIDGIN/accels $TMPPIDGIN/accels
echo "Sauvegarde du fichier $FOLDERPIDGIN/accels"

[ ! -f "$FOLDERPIDGIN/accounts.xml" ] || cp $FOLDERPIDGIN/accounts.xml $TMPPIDGIN/accounts.xml
echo "Sauvegarde du fichier $FOLDERPIDGIN/accounts.xml"

[ ! -f "$FOLDERPIDGIN/blist.xml" ] || cp $FOLDERPIDGIN/blist.xml $TMPPIDGIN/blist.xml
echo "Sauvegarde du fichier $FOLDERPIDGIN/blist.xml"

[ ! -f "$FOLDERPIDGIN/prefs.xml" ] || cp $FOLDERPIDGIN/prefs.xml $TMPPIDGIN/prefs.xml
echo "Sauvegarde du fichier $FOLDERPIDGIN/prefs.xml"

[ ! -f "$FOLDERPIDGIN/smileys.xml" ] || cp $FOLDERPIDGIN/smileys.xml $TMPPIDGIN/smileys.xml
echo "Sauvegarde du fichier $FOLDERPIDGIN/smileys.xml"

[ ! -f "$FOLDERPIDGIN/status.xml" ] || cp $FOLDERPIDGIN/status.xml $TMPPIDGIN/status.xml
echo "Sauvegarde du fichier $FOLDERPIDGIN/status.xml"

[ ! -f "$FOLDERPIDGIN/xmpp-caps.xml" ] || cp $FOLDERPIDGIN/xmpp-caps.xml $TMPPIDGIN/xmpp-caps.xml
echo "Sauvegarde du fichier $FOLDERPIDGIN/xmpp-caps.xml"
}

COMPRESSEUR() {
if [ -f /home/$USER/pidgin-$DATE.tar.xz ];then
    echo "/home/$USER/pidgin-$DATE.tar.xz existe"
    exit 0
else
    cd $TMPPIDGIN
    bsdtar cJf /home/$USER/pidgin-$DATE.tar.xz ./
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
$DIALOG --title "Sauvegarde de pidgin" --gauge "Traitement en cours..." 20 70 0

