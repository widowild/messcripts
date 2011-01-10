#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Histogramme des fréquences de chaque lettre dans un texte

nFich = raw_input('Nom du fichier : ')
fi = open(nFich, 'r')
# Conversion du fichier en une chaîne de caractères unicode.
# Suivant l'encodage du fichier source, activer l'une ou l'autre ligne :

#texte = fi.read().decode("Utf8")	
texte = fi.read().decode("Latin1")

fi.close()

print texte
dico ={}
for c in texte:                    # afin de les regrouper, on convertit
    c = c.upper()		   # toutes les lettres en majuscules
    dico[c] = dico.get(c, 0) +1

liste = dico.items()
liste.sort()
for car, freq in liste:
    print u"Caractère %s : %s occurrence(s)." % (car, freq)
