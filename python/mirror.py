#!/usr/bin/env python3
# -*- coding:Utf8 -*-
#=================
# Dépot mirror pour archlinux (32 bits et 64 bits)

## a faire:
# supprimer les dossiers en .~tmp~
# find /media/TERATOR/mirror/ -type d -name .~tmp~

import os
import time # pour convertir le time ctime en date plus lisible.
import sys # Pour quitter le programme
import subprocess # Appel de la commande subprocess.call()
import linecache # pour lire la 1ere ligne du fichier lastsync
import urllib.request # tester le site source

# Choix du site mirror
# Any
site = "mirrors.kernel.org"
# Great Britain
# site = "mirrors.uk2.net"
# Germany
# site = "ftp5.gwdg.de"

home, fichier, temporaire, lock, lastsync = "/media/TERATOR/mirror", "/files", "/tmp", "/tmp/mirrorsync.lck", "/lastsync"
target = home + fichier
tmp = home + temporaire
lastsync = target + lastsync
distribution = "archlinux"
source = site + "::" + distribution

# Affichage des données
print("Lieu du stockage :", home)
print("Dossier des fichiers :", target)
print("Source :", source)

# Tester le site.
req = urllib.request.Request("http://"+site)
try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(site, "hors ligne ou probleme de connexion")
    print(e.reason)
# suppression du fichier lock
    os.remove(lock)
    sys.exit()


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

# Calcul de l'heure entre les deux dépots:

    if os.path.isfile(lastsync): # test du fichier lastsync
        mirrorlastsync = urllib.request.urlopen("http://"+site+"/"+distribution+"/lastsync") # telechargement du fichier lastsync du miroir
        mlastsync = mirrorlastsync.read(100).decode('utf-8')
        mlastsync = int(mlastsync)
        # durée exprimée en string: 1289838601
        # donne en retour: Mon Nov 15 18:01:59 2010
        vlastsync = linecache.getline(lastsync,1).rstrip('\n')
        vlastsync = int(vlastsync)

        if vlastsync == mlastsync: # comparaison dépot et miroir
            print("le dépot est déjà à jour.")
            os.remove(lock)
            sys.exit()
        else :
            print("Non mis à jour depuis",(mlastsync - vlastsync) / 3600, "heures" )
            subprocess.call(['rsync', '-rtlvH', '--safe-links', '--delete-after', '--progress', '-h', '--delay-updates', '--no-motd', '--bwlimit=1000', '--temp-dir='+tmp , '--exclude=*.links.tar.gz*', '--exclude=/other', '--exclude=/sources', source, target])
            print("suppression du fichier", lock)
            os.remove(lock)
            print("Dernière mise à jour:", time.ctime(vlastsync))
            linecache.clearcache() # On vide le cache

else :
    print("Impossible d'exécuter le script")
    print("Veuillez supprimer", lock)
    sys.exit()
