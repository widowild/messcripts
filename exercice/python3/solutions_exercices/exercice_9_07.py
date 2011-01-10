#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Combinaison de deux fichiers texte pour en faire un nouveau

fichA = input("Nom du premier fichier : ")
fichB = input("Nom du second fichier : ")
fichC = input("Nom du fichier destinataire : ")
fiA = open(fichA, 'r')
fiB = open(fichB, 'r')
fiC = open(fichC, 'w')

while 1:
    ligneA = fiA.readline()    
    ligneB = fiB.readline()
    if ligneA =="" and ligneB =="":
        break               # On est arrivé à la fin des 2 fichiers
    if ligneA != "":
        fiC.write(ligneA)
    if ligneB != "":    
        fiC.write(ligneB)

fiA.close()
fiB.close()
fiC.close()