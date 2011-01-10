#! /usr/bin/env python
# -*- coding:Utf8 -*-

def chaineListe(ch):
    "convertit la chaîne ch en une liste de mots"
    ch = ch.decode("Utf8")      # conversion string => unicode
    liste, ct = [], u""         # ct est une chaîne temporaire unicode
    for c in ch:                # examiner tous les caractères de ch
        if c == " ":
            # lorsqu'on rencontre un espace, on ajoute la chaîne temporaire
            # à la liste, après l'avoir reconvertie en string :
            liste.append(ct.encode("Utf8"))
            ct = u""            # ... et on ré-initialise la chaîne temporaire
        else:
            # les autres caractères examinés sont ajoutés à la chaîne temp. :
            ct = ct + c
    # Ne pas oublier le mot restant après le dernier espace ! :      
    if ct:                      # vérifier si ct n'est pas une chaîne vide
        liste.append(ct.encode("Utf8"))
    return liste                # renvoyer la liste ainsi construite

# Tests :
if __name__ == '__main__':
    li = chaineListe("René est un garçon au caractère héroïque")
    print li
    for mot in li:
        print mot, "-",
    print chaineListe("")

