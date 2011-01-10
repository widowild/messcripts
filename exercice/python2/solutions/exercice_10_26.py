#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Mise en forme de donn�es num�riques
# Le fichier trait� est un fichier <texte> dont chaque ligne contient un nombre
# r�el (sans exposants et encod� sous la forme d'une cha�ne de caract�res)    

def arrondir(reel):
    "repr�sentation arrondie � .0 ou .5 d'un nombre r�el"
    ent = int(reel)             # partie enti�re du nombre
    fra = reel - ent            # partie fractionnaire
    if fra < .25 :
        fra = 0
    elif fra < .75 :
        fra = .5
    else:
        fra = 1
    return ent + fra    

fiSource = raw_input("Nom du fichier � traiter : ")
fiDest = raw_input("Nom du fichier destinataire : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')
while 1:
    ligne = fs.readline()
    if ligne == "" or ligne == "\n":
        break
    n = arrondir(float(ligne))      # conversion en <float>, puis arrondi
    fd.write(str(n) + "\n")         # enregistrement

fd.close()
fs.close()
