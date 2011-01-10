#! /usr/bin/env python
# -*- coding: Utf8 -*-

from exercice_10_10 import estUneMaj
from exercice_10_11 import chaineListe

def compteMaj(ch):
    "comptage des mots débutant par une majuscule dans la chaîne ch"
    c = 0
    lst = chaineListe(ch)       # convertir la phrase en une liste de mots
    for mot in lst:             # analyser chacun des mots de la liste
        if estUneMaj(mot[0]):
            c = c +1
    return c
    
# Test :
if __name__ == '__main__':
    phrase = "Les filles Tidgoutt se nomment Joséphine, Justine et Corinne"
    print("Phrase à tester : ", phrase)
    print("Cette phrase contient", compteMaj(phrase), "majuscules.")
