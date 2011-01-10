#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Le fichier trait� est un fichier texte dont chaque ligne contient un nombre
# r�el (sans exposants et encod� sous la forme d'une cha�ne de caract�res)    

def valArrondie(ch):
    "repr�sentation arrondie du nombre pr�sent� dans la cha�ne ch"
    f = float(ch)       # conversion de la cha�ne en un nombre r�el
    e = int(f + .5)     # conversion en entier (On ajoute d'abord
                        # 0.5 au r�el pour l'arrondir correctement)
    return str(e)       # reconversion en cha�ne de caract�res
     
fiSource = raw_input("Nom du fichier � traiter : ")
fiDest = raw_input("Nom du fichier destinataire : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')

while 1:
    ligne = fs.readline()       # lecture d'une ligne du fichier
    if ligne == "" or ligne == "\n":
        break
    ligne = valArrondie(ligne)
    fd.write(ligne +"\n")
    
fd.close()
fs.close()