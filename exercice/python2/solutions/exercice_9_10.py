#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Recherche de lignes particuli�res dans un fichier texte :

def chercheCP(ch):
    "recherche dans ch la portion de cha�ne contenant le code postal"
    i, f, ns = 0, 0, 0          # ns est un compteur de codes #
    cc = ""                     # cha�ne � construire 
    while i < len(ch):
        if ch[i] =="#":
            ns = ns +1
            if ns ==3:          # le CP se trouve apr�s le 3e code #
                f = 1           # variable "drapeau" (flag)
            elif ns ==4:        # inutile de lire apr�s le 4e code #
                break
        elif f ==1:             # le caract�re lu fait partie du
            cc = cc + ch[i]     # CP recherch� -> on m�morise
        i = i +1
    return cc    
        
nomF = raw_input("Nom du fichier � traiter : ")
codeP = raw_input("Code postal � rechercher : ")
fi = open(nomF, 'r')
while 1:
    ligne = fi.readline()
    if ligne =="":
        break
    if chercheCP(ligne) == codeP:
        print ligne
fi.close()
