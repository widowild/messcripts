#! /usr/bin/env python
# -*- coding: Latin-1 -*-

def tableMulti(n):
    # Fonction g�n�rant la table de multiplication par n (20 termes)
    # La table sera renvoy�e sous forme d'une cha�ne de caract�res :
    i, ch = 0, ""
    while i < 20:        
        i = i + 1
        ch = ch + str(i * n) + " "
    return ch

NomF = raw_input("Nom du fichier � cr�er : ")
fichier = open(NomF, 'w')

# G�n�ration des tables de 2 � 30 :
table = 2
while table < 31:
    fichier.write(tableMulti(table) + '\n')
    table = table + 1
fichier.close()