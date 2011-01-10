#! /usr/bin/env python
# -*- coding: Utf8 -*-

def convMajMin(ch):
    "échange les majuscules et les minuscules dans la chaîne ch"
    ch = ch.decode("Utf8")                # conversion -> unicode
    nouvC = u""                           # chaîne à construire
    for car in ch:
        code = ord(car)
        # les codes des maj. et min. sont séparés de 32 unités :
        if code >= 65 and code <= 91:     # majuscules ordinaires
            code = code + 32
        elif code >= 97 and code <= 122:  # minuscules ordinaires
            code = code - 32
        nouvC = nouvC + unichr(code)
    # renvoi de la chaine construite, reconvertie en string :
    return nouvC.encode("Utf8")

# test :
if __name__ == '__main__':
    print convMajMin("Roméo et Juliette")

