#! /usr/bin/env python
# -*- coding:Utf8 -*-

def estUnChiffre(car):
    "renvoie <vrai> si le caractère 'car' est un chiffre"
    if car in "0123456789":
        return "vrai"
    else:
        return "faux"

# Test :
if __name__ == '__main__':
    caracteres ="d75è8b0â1"
    print("Caractères à tester :", caracteres)
    for car in caracteres:
        print(car, estUnChiffre(car))

