#!/bin/bash


case "$1" in

progress)
    curr=`rhythmbox-client --no-start --print-playing-format "%te" | grep -v "Pas de lecture en cours"`
    tot=`rhythmbox-client --no-start --print-playing-format "%td" | grep -v "Pas de lecture en cours" | grep -v Inconnu`
    a=`date +'%S' | sed 's/^0\+//'`
if [ "$a" = "" ]; then
    a=0
fi
    b=$(( ($a*100) / 30 ))
    c=$(( 200-$b ))
#si pas de durée totale, augmente pendant les 30 premieres secondes puis diminue pendant les 30 suivantes...
    if [ "$tot" = "" ]; then 
    if [ $a -le 30 ]; then
       expr $b
    else
       expr $c
    fi
    else
#Si durée totale déterminée, il faut traiter le retour de la commande donnant $curr (pour courant et $tot pour total, logique) qui renvoit une donnée sous la forme hh:mm:ss
    d="1"
    nbcurr=`echo $curr | wc -m`       #nbr de caractères permet de déterminer si il y a seulement m:ss ou si il y a h:mm:ss (au minimum, m:ss)
    posm=$(( $nbcurr-5 ))             #pour faire une commande cut générique, il faut définir l'endroit ou on coupe d'ou posx (position des minutes ici)
if [ $posm -lt $d ]; then
posm=``                               #Si position inférieur à 1, renvoit variable vide pour ne pas bloque cut
fi
    posm2=$(( $nbcurr-4 ))            #Forcément 1 indication minute (minimum)= pas besoin de vérifier si >1
    posh=$(( $nbcurr-8 ))             #Idem pour les heures
if [ $posh -lt $d ]; then
posh=``
fi
    posh2=$(( $nbcurr-7 ))
    currs=`echo $curr | tail -c3 | sed 's/^0\+//'` # Récupération des secondes forcément à la fin et supression du premier 0 pour ne pas avoir de problème de base (08 en hexa ou base 10)
if [ "$currs" = "" ]; then
    currs=0                          #si uniquement des zeros, ils sont tous supprimé donc redonner la valeur
fi
    currma=`echo $curr | cut -c$posm-$posm2 | sed 's/^0\+//'`
if [ "$currma" = "" ]; then
    currma=0                         #idem pour minutes
fi
    currm=$(( $currma*60 ))          #conversion en secondes
if [ $posh2 -lt $d ]; then
currh=0
else
    currha=`echo $curr | cut -c$posh-$posh2 | sed 's/^0\+//'`
if [ "$currha" = "" ]; then         #idem heures
    currha=0
fi
currh=$(( $currha*3600 ))          # conversion en secondes
fi

    currt=$(( ($currh+$currm) + $currs )) #calcule du nombre de secondes total

    nbtot=`echo $tot | wc -m`      #Même schema pour la suite mais avec la durée totale
    tposm=$(( $nbtot-5 ))
if [ $tposm -lt $d ]; then
tposm=``
fi
    tposm2=$(( $nbtot-4 ))
    tposh=$(( $nbtot-8 ))
if [ $tposh -lt $d ]; then
tposh=``
fi
    tposh2=$(( $nbtot-7 ))
    tots=`echo $tot | tail -c3 | sed 's/^0\+//'` ## OK
if [ "$tots" = "" ]; then
    tots=0
fi
    totma=`echo $tot | cut -c$tposm-$tposm2 | sed 's/^0\+//'` ## OK
if [ "$totma" = "" ]; then
    totma=0
fi
    totm=$(( $totma*60 )) ## OK
if [ $tposh2 -lt $d ]; then
toth=0
else
    totha=`echo $tot | cut -c$tposh-$tposh2 | sed 's/^0\+//'` ## OK
if [ "$totha" = "" ]; then
    totha=0
fi
toth=$(( $totha*3600 )) ## OK
fi

    tott=$(( ($toth+$totm) + $tots )) ## OK
        expr $currt \* 100  / $tott    #Et finalement expression du pourcentage accompli
    fi
    ;;

esac
