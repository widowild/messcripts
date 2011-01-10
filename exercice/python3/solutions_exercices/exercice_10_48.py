#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Histogramme des fréquences de chaque mot dans un texte
# Suivant l'encodage du fichier source, activer l'une ou l'autre ligne :
encodage ="Latin-1"
#encodage ="Utf-8"

nFich = input('Nom du fichier à traiter ({}) : '.format(encodage))
# Conversion du fichier en une chaîne de caractères :
fi = open(nFich, 'r', encoding =encodage)
texte = fi.read()
fi.close()

# afin de pouvoir aisément séparer les mots du texte, on commence 
# par convertir tous les caractères non-alphabétiques en espaces  :
alpha = "abcdefghijklmnopqrstuvwxyzéèàùçâêîôûäëïöü"
lettres = ""            # nouvelle chaîne à construire
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
liste = list(dico.items())

# tri de la liste résultante :
liste.sort()
# affichage en clair :
for item in liste:
    print("{} : {}".format(item[0], item[1]))

