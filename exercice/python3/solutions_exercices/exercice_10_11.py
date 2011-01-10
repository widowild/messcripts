#! /usr/bin/env python
# -*- coding:Utf8 -*-

def chaineListe(ch):
    "convertit la chaîne ch en une liste de mots"
    liste, ct = [], ""          # ct est une chaîne temporaire
    for c in ch:                # examiner tous les caractères de ch
        if c == " ":            # lorsqu'on rencontre un espace,
            liste.append(ct)    # on ajoute la chaîne temporaire à la liste
            ct = ""             # ... et on ré-initialise la chaîne temporaire
        else:
            # les autres caractères examinés sont ajoutés à la chaîne temp. :
            ct = ct + c
    # Ne pas oublier le mot restant après le dernier espace ! :      
    if ct:                      # vérifier si ct n'est pas une chaîne vide
        liste.append(ct)
    return liste                # renvoyer la liste ainsi construite

# Tests :
if __name__ == '__main__':
    li = chaineListe("René est un garçon au caractère héroïque")
    print(li)
    for mot in li:
        print(mot, "-", end=' ')
    print(chaineListe(""))              # doit renvoyer une liste vide

