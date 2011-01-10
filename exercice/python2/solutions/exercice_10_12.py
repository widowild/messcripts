#! /usr/bin/env python
# -*- coding:Utf8 -*-

from exercice_10_10 import majuscule
from exercice_10_11 import chaineListe

txt = "Le prénom de cette Dame est Élise"
lst = chaineListe(txt)          # convertir la phrase en une liste de mots
for mot in lst:                 # analyser chacun des mots de la liste
    # Pour extraire le premier caractère du mot, il faut passer par unicode,
    # sinon les caractères accentués ne seront pas corrects :
    motU = mot.decode("Utf8")   # conversion -> unicode
    prem = motU[0]              # extraction du premier caractère
    prem = prem.encode("Utf8")  # re-conversion -> string
    if majuscule(prem):         # test de majuscule
        print mot

# Variante plus compacte, utilisant la composition :
for mot in lst:
    if majuscule(mot.decode("Utf8")[0].encode("Utf8")):
        print mot
