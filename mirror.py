#!/usr/bin/env python3
# -*- coding:Utf8 -*-
#=================
# Dépot mirror pour archlinux (32 bits et 64 bits)

import os
import time # pour convertir le time ctime en date plus lisible.
import sys # Pour quitter le programme
import subprocess # Appel de la commande subprocess.call()
import linecache # pour lire la 1ere ligne du fichier lastsync

home, fichier, temporaire, lock, lastsync = "/media/TERATOR/mirror", "/files", "/tmp", "/tmp/mirrorsync.lck", "/lastsync"
target = home + fichier
tmp = home + temporaire
lastsync = target + lastsync
source = 'mirrors.uk2.net::archlinux'

# Affichage des données
print("Lieu du stockage :", home)
print("Dossier des fichiers :", target)
print("Source :", source)

# Creation des dossiers si besoin
try:
    if not os.path.isdir(target): # test de l'existence du dossier target
        os.makedirs(target) # Creation du dossier target
        print(target, "crée")
except:
    print("Impossible d'acceder ou de créer le dossier ", target)

try:
    if not os.path.isdir(tmp): # test de l'existence du dossier tmp
        os.makedirs(tmp) # Creation du dossier tmp
        print(tmp, "crée")
except:
    print("Impossible d'acceder ou de créer le dossier", tmp)

if not os.path.isfile(lock): # test existence d'un fichier
    print("creation du fichier", lock)
    open(lock,"w") # creer un fichier lock
    subprocess.call(['rsync', '-rtlvH', '--safe-links', '--delete-after', '--progress', '-h', '--delay-updates', '--no-motd', '--bwlimit=1000', '--temp-dir='+tmp , "--exclude='*.links.tar.gz*'", "--exclude='/other'", "--exclude='/sources'", source, target])
    print("suppression du fichier", lock)
    os.remove(lock)

    if os.path.isfile(lastsync): # test du fichier lastsync
        # durée exprimée en string: 1289838601
        # donne en retour: Mon Nov 15 18:01:59 2010
        vlastsync = linecache.getline(lastsync,1).rstrip('\n')
        vlastsync = int(vlastsync)
        print(time.ctime(vlastsync))
        linecache.clearcache() # On vide le cache

else :
    print("Impossible d'exécuter le script")
    print("Veuillez supprimer", lock)
    sys.exit()
