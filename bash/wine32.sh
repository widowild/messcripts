#!/bin/bash
echo "Lancement environnement Wine pour plateforme 32 bits"

if [ $# -eq 0 ]; then
    printf "Syntaxe: $0 /dossier/jeu.exe\n" >&2
    exit 1
fi
dossier=/home/$USER/win32
[ -d /home/$USER/win32 ] || echo "$dossier n'existe pas"
WINEARCH=win32 WINEPREFIX=$dossier wine "$@"
