#!/usr/bin/env python
# -*- coding:Utf-8 -*-

import subprocess, os

volume = ['80', '0']
print("volume maximal:", volume[0], "%") # afficher la valeur maximum
print("volume minimal:", volume[1], "%") # afficher la valeur minumum

p = os.system("amixer scontrols |cut -d',' -f1 | sed -e "s/'//g" |awk '{print $4, $5, $6}'")
print(p)
#amixer scontrols |cut -d',' -f1 | sed -e "s/'//g" |awk '{print $4, $5, $6}' | sort | uniq >> /tmp/amixer.log

#while read ligne
#do
#    amixer -q set "$ligne" $VOLUME% unmute
#    echo "Canal "$ligne" activé Volume $VOLUME%"
#    done < /tmp/amixer.log
#rm /tmp/amixer.log

#====    Canal Muet ====#
#    amixer -q set "Analog Mix" 0% unmute
#    amixer -q set "Beep" 0% unmute
