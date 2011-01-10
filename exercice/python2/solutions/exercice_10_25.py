#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Le fichier de d�part est un fichier <texte> dont chaque ligne contient
# un nombre r�el (encod� sous la forme d'une cha�ne de caract�res)    

from math import pi

def caractSphere(d):
    "renvoie les caract�ristiques d'une sph�re de diam�tre d"
    d = float(d)        # conversion de l'argument (=cha�ne) en r�el
    r = d/2             # rayon
    ss = pi*r**2        # surface de section
    se = 4*pi*r**2      # surface ext�rieure
    v = 4./3*pi*r**3    # volume (! la premi�re division doit �tre r�elle !)
    # Le marqueur de conversion %8.2f utilis� ci-dessous formate le nombre
    # affich� de mani�re � occuper 8 caract�res au total, en arrondissant
    # de mani�re � conserver deux chiffres apr�s la virgule : 
    ch = "Diam. %6.2f cm Section = %8.2f cm� " % (d, ss)
    ch = ch +"Surf. = %8.2f cm�. Vol. = %9.2f cm�" % (se, v)
    return ch

fiSource = raw_input("Nom du fichier � traiter : ")
fiDest = raw_input("Nom du fichier destinataire : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')
while 1:
    diam = fs.readline()
    if diam == "" or diam == "\n":
        break
    fd.write(caractSphere(diam) + "\n")         # enregistrement
fd.close()
fs.close()
