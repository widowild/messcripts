#! /usr/bin/env python
# -*- coding: Latin-1 -*-

def compteCar(ca, ch):
    "Renvoie le nombre de caract�res ca trouv�s dans la cha�ne ch"
    i, tot = 0, 0
    while i < len(ch):
        if ch[i] == ca:
            tot = tot + 1
        i = i + 1
    return tot    
        
# test :
print compteCar("e","Cette cha�ne est un exemple")
