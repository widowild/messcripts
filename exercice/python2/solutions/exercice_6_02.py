#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# P�rim�tre et Aire d'un triangle quelconque

from math import sqrt

print "Veuillez entrer le c�t� a : "
a = float(raw_input())
print "Veuillez entrer le c�t� b : "
b = float(raw_input())
print "Veuillez entrer le c�t� c : "
c = float(raw_input())
d = (a + b + c)/2                # demi-p�rim�tre
s = sqrt(d*(d-a)*(d-b)*(d-c))    # aire (suivant formule)

print "Longueur des c�t�s =", a, b, c
print "P�rim�tre =", d*2, "Aire =", s