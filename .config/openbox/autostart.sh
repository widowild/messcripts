#! /bin/bash
# Fond d'écran (souvenir)
eval `cat ~/.fehbg` &amp;
# Ajouter des ombres au fenetre
#xcompmgr -c -f &amp;
# barre de tâches
#pypanel &amp;
# Boinc
#/home/wido/.script/run_client &amp;
#Audio
(sleep 10 && /home/wido/.script/volumealsa2.sh) &amp;
# Mpd
/home/wido/.mpd/mpd_boot.sh &amp;
# Conky
/home/wido/.conky/conkystart.sh &amp;

# Barre de tâches
# bmpanel theme &amp;
#bmpanel darkblack18 &amp;
tint2 &amp;
# guake terminal à la quake (F12)
guake &amp;
