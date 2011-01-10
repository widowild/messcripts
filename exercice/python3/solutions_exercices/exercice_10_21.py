#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Conversion en majuscule du premier caractère de chaque mot dans un texte.

fiSource = input("Nom du fichier à traiter (Latin-1) : ")
fiDest = input("Nom du fichier destinataire (Utf-8) : ")
fs = open(fiSource, 'r', encoding ="Latin1")
fd = open(fiDest, 'w', encoding ="Utf8")

while 1:
    ch = fs.readline()                   # lecture d'une ligne
    if ch == "":
        break                            # fin du fichier
    ch = ch.title()                      # conversion des initiales en maj.
    fd.write(ch)                         # transcription

fd.close()    
fs.close()


