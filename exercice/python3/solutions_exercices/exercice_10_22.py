#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Conversion Latin-1 => Utf8 (variante utilisant une variable <bytes>

fiSource = input("Nom du fichier à traiter (Latin-1) : ")
fiDest = input("Nom du fichier destinataire (Utf-8) : ")
fs = open(fiSource, 'rb')            # mode de lecture <binaire>
fd = open(fiDest, 'wb')              # mode d'écriture <binaire>

while 1:
    so = fs.readline()               # la ligne lue est une séquence d'octets
    # Remarque : la variable so étant du type <bytes>, on doit la comparer
    # avec une chaîne littérale (vide) du même type dans les tests :  
    if so == b"":
        break                        # fin du fichier
    ch = so.decode("Latin-1")        # conversion en chaîne de caractères
    ch = ch.replace(" ","-*-")       # remplacement des espaces par -*-
    so = ch.encode("Utf-8")          # Ré-encodage en une séquence d'octets
    fd.write(so)                     # transcription

fd.close()    
fs.close()


