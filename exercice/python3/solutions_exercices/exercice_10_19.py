#! /usr/bin/env python
# -*- coding:Utf-8 -*-

from exercice_10_18 import voyelle

def compteVoyelles(phrase):
    "compte les voyelles présentes dans la chaîne de caractères <phrase>"
    n = 0
    for c in phrase:
        if voyelle(c):
            n = n + 1
    return n

# Test :
if __name__ == '__main__':
    texte ="Maître corbeau sur un arbre perché"
    nv = compteVoyelles(texte)
    print("La phrase <", texte, "> compte ", nv, " voyelles.", sep="")
