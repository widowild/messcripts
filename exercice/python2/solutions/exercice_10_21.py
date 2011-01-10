#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Conversion en majuscule du premier caractère de chaque mot dans un texte

fiSource = raw_input("Nom du fichier à traiter (Latin-1) : ")
fiDest = raw_input("Nom du fichier destinataire (Utf-8) : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')

while 1:
    ch = fs.readline().decode("Latin1")  # lecture d'une ligne
    if ch == "":
        break                            # fin du fichier
    ch = ch.title()                      # conversion des initiales en maj.
    fd.write(ch.encode("Utf8"))          # transcription

fd.close()    
fs.close()
