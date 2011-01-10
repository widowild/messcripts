#! /usr/bin/env python
# -*- coding:Utf-8 -*-

from exercice_10_18 import voyelle

def compteVoyelles(chu):
    "compte les voyelles présentes dans la chaîne unicode chu"
    n = 0
    for c in chu:
        if voyelle(c):
            n = n + 1
    return n

# Test :
if __name__ == '__main__':
    phrase ="Maître corbeau sur un arbre perché"
    nv = compteVoyelles(phrase.decode("Utf8"))
    print "La phrase", phrase, "compte", nv, "voyelles."
