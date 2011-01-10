#! /usr/bin/env python
# -*- coding:Utf8 -*-

from exercice_10_10 import estUneMaj
from exercice_10_11 import chaineListe

txt = "Le prénom de cette Dame est Élise"
print("Phrase à tester :", txt)

lst = chaineListe(txt)          # convertir la phrase en une liste de mots

for mot in lst:                 # analyser chacun des mots de la liste
    prem = mot[0]               # extraction du premier caractère
    if estUneMaj(prem):         # test de majuscule
        print(mot)

# Variante plus compacte, utilisant la composition :
print("Variante :")
for mot in lst:
    if estUneMaj(mot[0]):
        print(mot)
