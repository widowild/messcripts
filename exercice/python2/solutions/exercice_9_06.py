#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Comparaison de deux fichiers, caract�re par caract�re :

fich1 = raw_input("Nom du premier fichier : ")
fich2 = raw_input("Nom du second fichier : ")
fi1 = open(fich1, 'r')
fi2 = open(fich2, 'r')

c, f = 0, 0                 # compteur de caract�res et "drapeau" 
while 1:
    c = c + 1
    car1 = fi1.read(1)      # lecture d'un caract�re dans chacun
    car2 = fi2.read(1)      # des deux fichiers
    if car1 =="" or car2 =="":
        break
    if car1 != car2 :
        f = 1
        break               # diff�rence trouv�e

fi1.close()
fi2.close()

print "Ces 2 fichiers",
if f ==1:
    print "diff�rent � partir du caract�re n�", c
else:
    print "sont identiques."
