#! /usr/bin/env python
# -*- coding:Utf8 -*-

def chiffre(car):
    "renvoie <vrai> si le caractère 'car' est un chiffre"
    # Cette fonction accepte indifféremment des caractères 'string' ou
    # 'unicode', car les identifiants numériques associés aux chiffres sont
    # les mêmes dans toutes les normes d'encodage.
    if car in "0123456789":
        return 1
    else:
        return 0

# Test :
if __name__ == '__main__':
    print chiffre('d'), chiffre('7'), chiffre(u'5'), chiffre(u'é')
