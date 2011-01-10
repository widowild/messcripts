#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Rechercher l'indice d'un caract�re donn� dans une cha�ne

def trouve(ch, car, deb=0):
    "trouve l'indice du caract�re car dans la cha�ne ch"
    i = deb
    while i < len(ch):
        if ch[i] == car:
            return i		# le caract�re est trouv� -> on termine
        i = i + 1
    return -1       		# toute la cha�ne a �t� scann�e sans succ�s 

# Test :
if __name__ == '__main__':
    print trouve("Coucou c'est moi", "z")
    print trouve("Juliette & Rom�o", "&")
    print trouve("C�sar & Cl�op�tre", "r", 5)
