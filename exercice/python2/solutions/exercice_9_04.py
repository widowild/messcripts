#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Ce script montre �galement comment modifier le contenu d'un fichier
# en le transf�rant d'abord tout entier dans une liste, puis en
# r�enregistrant celle-ci apr�s modifications

def triplerEspaces(ch):
    "fonction qui triple les espaces entre mots dans la cha�ne ch"
    i, nouv = 0, ""
    while i < len(ch):
        if ch[i] == " ":
            nouv = nouv + "   "
        else:
            nouv = nouv + ch[i]
        i = i +1    
    return nouv

NomF = raw_input("Nom du fichier : ")
fichier = open(NomF, 'r+')              # 'r+' = mode read/write
lignes = fichier.readlines()            # lire toutes les lignes

n=0
while n < len(lignes):
    lignes[n] = triplerEspaces(lignes[n])
    n =n+1
    
fichier.seek(0)                         # retour au d�but du fichier
fichier.writelines(lignes)              # r�enregistrement
fichier.close()
