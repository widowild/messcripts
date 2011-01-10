#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Simple �diteur de texte

def sansDC(ch):
    "cette fonction renvoie la cha�ne ch amput�e de son dernier caract�re"
    nouv = ""
    i, j = 0, len(ch) -1
    while i < j:
        nouv = nouv + ch[i]
        i = i + 1
    return nouv

def ecrireDansFichier():
    of = open(nomF, 'a')
    while 1:
        ligne = raw_input("entrez une ligne de texte (ou <Enter>) : ")
        if ligne == '':
            break
        else:
            of.write(ligne + '\n')
    of.close()

def lireDansFichier():
    of = open(nomF, 'r')
    while 1:
        ligne = of.readline()
        if ligne == "":
            break
        # afficher en omettant le dernier caract�re (= fin de ligne) :
        print sansDC(ligne)
    of.close()

nomF = raw_input('Nom du fichier � traiter : ')
choix = raw_input('Entrez "e" pour �crire, "c" pour consulter les donn�es : ')

if choix =='e':
    ecrireDansFichier()
else:
    lireDansFichier()
