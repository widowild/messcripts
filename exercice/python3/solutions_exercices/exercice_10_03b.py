#! /usr/bin/env python
# -*- coding: Utf8 -*-

# Rechercher l'indice d'un caractère donné dans une chaîne

def trouve(ch, car, deb=0):
    "trouve l'indice du caractère car dans la chaîne ch"
    ch = ch.decode("Utf8")      # conversion 'string' => 'unicode'
    i = deb
    while i < len(ch):
        if ch[i] == car:
            return i		# le caractère est trouvé -> on termine
        i = i + 1
    return -1       		# toute la chaîne a été scannée sans succès 

# Test :
if __name__ == '__main__':
    print(trouve("Coucou c'est moi", "z"))
    print(trouve("Juliette & Roméo", "&"))
    print(trouve("César & Cléopâtre", "r", 5))
