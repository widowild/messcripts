#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Histogramme des fréquences de chaque lettre dans un texte

nFich = input('Nom du fichier (Latin-1) : ')
fi = open(nFich, 'r', encoding ="Latin1")
texte = fi.read()
fi.close()

print(texte)
dico ={}
for c in texte:                    # afin de les regrouper, on convertit
    c = c.upper()		           # toutes les lettres en majuscules
    dico[c] = dico.get(c, 0) +1

liste = list(dico.items())
liste.sort()
for car, freq in liste:
    print("Caractère {} : {} occurrence(s).".format(car, freq))
