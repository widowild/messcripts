#! /usr/bin/env python
# -*- coding:Utf8 -*-

from math import sqrt                # fonction racine carrée

def distance(p1, p2):
    # On applique le théorème de Pythagore :
    dx =abs(p1.x - p2.x)             # abs() => valeur absolue
    dy =abs(p1.y - p2.y)
    return sqrt(dx*dx + dy*dy)

def affiche_point(p):
    print("Coord. horiz.", p.x, "Coord. vert.", p.y) 

class Point(object):
    "Classe de points géométriques"

# Définition des 2 points :
p8, p9 = Point(), Point()
p8.x, p8.y, p9.x, p9.y = 12.3, 5.7, 6.2, 9.1

affiche_point(p8)
affiche_point(p9)
print("Distance =", distance(p8,p9))



