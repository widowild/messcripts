#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Histogramme des fréquences de chaque mot dans un texte

nFich = raw_input('Nom du fichier à traiter : ')
fi = open(nFich, 'r')
# Conversion du fichier en une chaîne de caractères unicode.
# Suivant l'encodage du fichier source, activer l'une ou l'autre ligne :

texte = fi.read().decode("Utf8")	
#texte = fi.read().decode("Latin1")

fi.close()

# afin de pouvoir aisément séparer les mots du texte, on commence 
# par convertir tous les caractères non-alphabétiques en espaces  :

alpha = u"abcdefghijklmnopqrstuvwxyzéèàùçâêîôûäëïöü"

lettres = u""           # nouvelle chaîne à construire (unicode)
for c in texte:
    c = c.lower()       # conversion de chaque caractère en minuscule
    if c in alpha:
        lettres = lettres + c
    else:
        lettres = lettres + ' '

# conversion de la chaîne résultante en une liste de mots :
mots = lettres.split()

# construction de l'histogramme :
dico ={}
for m in mots:
    dico[m] = dico.get(m, 0) +1

liste = dico.items()

# tri de la liste résultante :
liste.sort()

# affichage en clair :
for item in liste:
    print item[0], ":", item[1]
