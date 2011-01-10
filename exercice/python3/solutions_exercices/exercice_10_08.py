#! /usr/bin/env python
# -*- coding:Utf8 -*-

def compteCar(ch, car):
    "comptage du nombre de caractères <car> la chaîne <ch>"
    if len(ch) ==0:
        return 0
    n =0
    for c in ch:
        if c == car:
            n = n + 1
    return n

# Programme principal :

def compteCarDeListe(chaine, serie):
    "dans la chaine <ch>, comptage du nombre de caractères listés dans <serie>"
    for cLi in serie:
        nc =compteCar(chaine, cLi)
        print("Caractère", cLi, ":", nc)


# Test :
if __name__ == '__main__':
    txt ="René et Célimène étaient eux-mêmes nés à Noël de l'année dernière"
    print(txt)
    compteCarDeListe(txt, "eéèêë")
