#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Utilisation d'une liste et de branchements conditionnels

print("Ce script recherche le plus grand de trois nombres")
print('Veuillez entrer trois nombres séparés par des virgules : ')
# Note : la fonction list() convertit en liste la séquence de données qu'on
# lui fournit en argument. La fonction eval() convertit une chaîne de car.
# en une expression Python. Or, N valeurs numériques séparées par des virgules
# constituent un tuple Python. L'instruction ci-dessous convertira donc les
# données fournies par l'utilisateur en une liste  nn :
nn = list(eval(input()))
max, index = nn[0], 'premier'
if nn[1] > max:			# ne pas omettre le double point !
    max = nn[1]
    index = 'second'
if nn[2] > max:
    max = nn[2]
    index = 'troisième'
print("Le plus grand de ces nombres est", max)
print("Ce nombre est le", index, "de votre liste.")
