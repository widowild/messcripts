#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Utilisation d'une liste et de branchements conditionnels

print "Ce script recherche le plus grand de trois nombres"
print 'Veuillez entrer trois nombres s�par�s par des virgules : '
# Note : la fonction list() convertit en liste la s�quence de donn�es qu'on
# lui fournit en argument. L'instruction ci-dessous convertira donc les
# donn�es fournies par l'utilisateur en une liste  nn :
nn = list(input())
max, index = nn[0], 'premier'
if nn[1] > max:			# ne pas omettre le double point !
    max = nn[1]
    index = 'second'
if nn[2] > max:
    max = nn[2]
    index = 'troisi�me'
print "Le plus grand de ces nombres est", max
print "Ce nombre est le", index, "de votre liste."
