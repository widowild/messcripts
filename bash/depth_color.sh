#!/bin/bash 
# Interface GUI pour changer le nombre de couleur (color depth)

#Dependance: Zenity

if [ ! "$(which zenity)" ]; then 
   echo "Zenity n'est pas installé" 
zenity --error --title "Erreur dépendance" --text "Zenity n'est pas installé"
   exit 1 
fi

if [ ! -f "/etc/X11/xorg.conf" ]; then 
   echo "/etc/X11/xorg.conf n'existe pas" 
zenity --error --title "Problème de fichier" --text "/etc/X11/xorg.conf n'existe pas"
   exit 1 
fi

VALEURDEFAUT=$(cat /etc/X11/xorg.conf | grep DefaultDepth | awk '{print $2}')

SUDO ()
{
sudo -K
zenity --entry --hide-text --text="Veuillez donner le mot de passe Sudo" | sudo -S -s


if [ "$?" = 1 ]; then
    zenity --info --text="Erreur" --title "Erreur";
    exit 1
else
    KILL_SERVEUR
fi

}

# Redémarrage du serveur X:
KILL_SERVEUR () {

if [ -f "/etc/init.d/gdm" ]; then
    {
       cp /tmp/xorg.conf.bak /etc/X11/xorg.conf && /etc/init.d/gdm restart
}
elif [ -f "/etc/rc.d/gdm" ]; then
    {
       cp /tmp/xorg.conf.bak /etc/X11/xorg.conf && /etc/rc.d/gdm restart
}

elif [ -f "/etc/init.d/kdm" ]; then
    {        
        cp /tmp/xorg.conf.bak /etc/X11/xorg.conf && /etc/init.d/kdm restart
}
elif [ -f "/etc/rc.d/kdm" ]; then
    {        
        cp /tmp/xorg.conf.bak /etc/X11/xorg.conf && /etc/rc.d/kdm restart
}

elif [ -f "/etc/init.d/xdm" ]; then
    {    
        cp /tmp/xorg.conf.bak /etc/X11/xorg.conf && /etc/init.d/xdm restart
}
elif [ -f "/etc/rc.d/xdm" ]; then
    {        
        cp /tmp/xorg.conf.bak /etc/X11/xorg.conf && /etc/rc.d/xdm restart
}
elif [ -f "/etc/rc.d/slim" ]; then
    {
        cp /tmp/xorg.conf.bak /etc/X11/xorg.conf && /etc/rc.d/slim restart
}
else
    echo "Le serveur graphique n'est pas reconnu par le script."
zenity --error --title "Erreur dépendance" --text "Le serveur graphique n'est pas reconnu par le script."
fi
}

# Choix de resolution de couleur: (8,16,24)

choix=$(zenity --list --radiolist \
    --title="Choisissez la résolution" \
  --column="" --column="Résolution" --column="Description" \
   "FALSE"  "8" "Depth 8" \
   "FALSE" "16" "Depth 16" \
   "TRUE" "24" "Depth 24" )

if [ "$choix" = "8" ]; then
{
echo "Vous remplacez la résolution $VALEURDEFAUT par $choix"
sed -e '/DefaultDepth/c\        DefaultDepth 8'    /etc/X11/xorg.conf > /tmp/xorg.conf.bak
zenity --question --text "Etes vous sure de redemarrer le serveur X?"; echo $?
if [ "$?" = 1 ]; then
    zenity --info --text="Le redémarrage a été annulée" --title "Annulation";
    exit 1
else
    SUDO
fi

}
elif [ "$choix" = "16" ]; then
{
echo "Vous remplacez la résolution $VALEURDEFAUT par $choix"
sed -e '/DefaultDepth/c\        DefaultDepth 16'    /etc/X11/xorg.conf > /tmp/xorg.conf.bak
zenity --question --text "Etes vous sure de redemarrer le serveur X?";

if [ "$?" = 1 ]; then
    zenity --info --text="Le redémarrage a été annulée" --title "Annulation";
    exit 1
else
    SUDO
fi
}
else [ "$choix" = "24" ]
{
echo "Vous remplacez la résolution $VALEURDEFAUT par $choix"
sed -e '/DefaultDepth/c\        DefaultDepth 24'    /etc/X11/xorg.conf > /tmp/xorg.conf.bak
zenity --question --text "Etes vous sure de redemarrer le serveur X?";
if [ "$?" = 1 ]; then
    zenity --info --text="Le redémarrage a été annulée" --title "Annulation";
    exit 1
else 
    SUDO
fi
}
fi
