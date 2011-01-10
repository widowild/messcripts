#! /usr/bin/env python
# -*- coding: Utf8 -*-

def decoupe(ch, n):
    "découpage de la chaîne ch en une liste de fragments de n caractères"
    ch =ch.decode("Utf8")    # Conversion 'string' => 'unicode'
    d, f = 0, n              # indices de début et de fin de fragment
    tt = []                  # liste à construire
    while d < len(ch):
        if f > len(ch):      # on ne peut pas découper au-delà de la fin
            f = len(ch)
        fr = ch[d:f]         # découpage d'un fragment
        tt.append(fr)        # ajout du fragment à la liste
        d, f = f, f +n       # indices suivants 
    return tt

def inverse(tt):
    "rassemble les éléments de la liste tt dans l'ordre inverse"
    ch = ""                  # chaîne à construire
    i = len(tt)              # on commence par la fin de la liste
    while i > 0 :
        i = i - 1            # le dernier élément possède l'indice n -1
        ch = ch + tt[i]
    return ch

# Test :
if __name__ == '__main__':
    ch ="abcdefghijklmnopqrstuvwxyz123456789âêîôûàèìòùáéíóú"
    print ch
    liste = decoupe(ch, 5)
    print liste
    print inverse(liste)

