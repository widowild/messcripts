#!/bin/bash
echo "Lancement environnement Wine pour plateforme 64 bits"

if [ $# != 1 ]
then
    printf "Syntaxe: $0 /dossier/jeu.exe\n" >&2
    exit 1
fi

dossier=/home/$USER/win64
[ -d $dossier ] || echo "$dossier n'existe pas"

WINEARCH=win32 WINEPREFIX=$dossier wine "$1"
