#! /usr/bin/env python
# -*- coding:Utf-8 -*-

####################################################
# Conversion en Utf-8 de textes encodés en Latin-9 #
####################################################

import os, sys

def findOptions():
    options = sys.argv
    lo =len(options)
    if lo ==2:
        return options[1]
    print "\n******** Erreur ********************************\n"\
          "Usage : ./convutf8.py nom_du_fichier_a_convertir\n"\
          "************************************************\n"
    sys.exit()

fichier =findOptions()
of =open(fichier, "r")
ll = of.readlines()
of.close()

of =open(fichier, "w")
for l in ll:
    lt =l.decode("Latin-1").encode("Utf-8")
    of.write(lt)
of.close()

print "\nLe fichier %s a été ré-encodé de Latin-1 en Utf-8.\n" % fichier