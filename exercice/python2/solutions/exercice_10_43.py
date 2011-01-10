#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Test du g�n�rateur de nombres al�atoires

from random import random           # tire au hasard un r�el entre 0 et 1

n = raw_input("Nombre de valeurs � tirer au hasard (d�faut = 1000) : ")
if n == "":
    nVal =1000
else:
    nVal = int(n)

n = raw_input("Nombre de fractions dans l'intervalle 0-1 (entre 2 et "
              + str(nVal/10) + ", d�faut =5) : ")
if n == "":
    nFra =5
else:
    nFra = int(n)

if nFra < 2:
    nFra =2
elif nFra > nVal/10:
    nFra = nVal/10

print "Tirage au sort des", nVal, "valeurs ..."
listVal = [0]*nVal                      # cr�er une liste de z�ros
for i in range(nVal):                   # puis modifier chaque �l�ment
    listVal[i] = random()

print "Comptage des valeurs dans chacune des", nFra, "fractions ..."
listCompt = [0]*nFra                    # cr�er une liste de compteurs

# parcourir la liste des valeurs :
for valeur in listVal:
    # trouver l'index de la fraction qui contient la valeur :    
    index = int(valeur*nFra)
    # incr�menter le compteur correspondant :
    listCompt[index] = listCompt[index] +1

# afficher l'�tat des compteurs :
for compt in listCompt:
    print compt,
