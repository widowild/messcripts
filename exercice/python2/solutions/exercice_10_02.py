#! /usr/bin/env python
# -*- coding: Latin-1 -*-

def decoupe(ch, n):
    "d�coupage de la cha�ne ch en une liste de fragments de n caract�res"
    d, f = 0, n             # indices de d�but et de fin de fragment
    tt = []                 # liste � construire
    while d < len(ch):
        if f > len(ch):     # on ne peut pas d�couper au-del� de la fin
            f = len(ch)
        fr = ch[d:f]        # d�coupage d'un fragment
        tt.append(fr)       # ajout du fragment � la liste
        d, f = f, f +n      # indices suivants 
    return tt

def inverse(tt):
    "rassemble les �l�ments de la liste tt dans l'ordre inverse"
    ch = ""                 # cha�ne � construire
    i = len(tt)             # on commence par la fin de la liste
    while i > 0 :
        i = i - 1           # le dernier �l�ment poss�de l'indice n -1
        ch = ch + tt[i]
    return ch

# Test :
if __name__ == '__main__':
    ch ="abcdefghijklmnopqrstuvwxyz123456789"
    liste = decoupe(ch, 5)
    print liste
    print inverse(liste)