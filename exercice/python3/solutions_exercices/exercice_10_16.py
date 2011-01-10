#! /usr/bin/env python
# -*- coding: Utf8 -*-

def convMajMin(ch):
    "échange les majuscules et les minuscules dans la chaîne ch"
    nouvC = ""                               # chaîne à construire
    for car in ch:
        code = ord(car)
        # les codes numériques des caractères majuscules et minuscules
        # correspondants sont séparés de 32 unités :
        if code >= 65 and code <= 91:        # majuscules ordinaires
            code = code + 32
        elif code >= 192 and code <= 222:    # majuscules accentuées
            code = code + 32
        elif code >= 97 and code <= 122:     # minuscules ordinaires
            code = code - 32
        elif code >= 224 and code <= 254:    # minuscules accentuées
            code = code - 32
        nouvC = nouvC + chr(code)
    # renvoi de la chaîne construite :
    return nouvC

# test :
if __name__ == '__main__':
    txt ="Émile Noël épouse Irène Müller"
    print(txt)
    print(convMajMin(txt))

