#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Le fichier de départ est un fichier <texte> dont chaque ligne contient
# un nombre réel (encodé sous la forme d'une chaîne de caractères)    

from math import pi

def caractSphere(d):
    "renvoie les caractéristiques d'une sphère de diamètre d"
    d = float(d)        # conversion de l'argument (=chaîne) en réel
    r = d/2             # rayon
    ss = pi*r**2        # surface de section
    se = 4*pi*r**2      # surface extérieure
    v = 4/3*pi*r**3     # volume
    # La balise {:8.2f} utilisé ci-dessous formate le nombre
    # affiché de manière à occuper 8 caractères au total, en arrondissant
    # de manière à conserver deux chiffres après la virgule : 
    ch = "Diam. {:6.2f} cm Section = {:8.2f} cm² ".format(d, ss)
    ch = ch +"Surf. = {:8.2f} cm². Vol. = {:9.2f} cm³".format(se, v)
    return ch

fiSource = input("Nom du fichier à traiter : ")
fiDest = input("Nom du fichier destinataire : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')
while 1:
    diam = fs.readline()
    if diam == "" or diam == "\n":
        break
    fd.write(caractSphere(diam) + "\n")         # enregistrement
fd.close()
fs.close()
