#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Utilisation d'une petite base de donn�es acceptant les requ�tes SQL

import gadfly
import os

chemin = os.getcwd()        # Obtention du r�pertoire courant

baseDonn = gadfly.gadfly("musique", chemin)
cur = baseDonn.cursor()
while 1:
    print "Veuillez entrer votre requ�te SQL (ou <Enter> pour terminer) :"
    requete = raw_input()
    if requete =="":
        break
    try:
        cur.execute(requete)        # ex�cution de la requ�te SQL
    except:
        print '*** Requ�te incorrecte ***'
    else:    
        print cur.pp()              # Affichage du r�sultat
    print

choix = raw_input("Confirmez-vous l'enregistrement (o/n) ? ")
if choix[0] == "o" or choix[0] == "O":
    baseDonn.commit()
else:
    baseDonn.close()

