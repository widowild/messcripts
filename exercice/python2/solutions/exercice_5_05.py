#! /usr/bin/env python
# -*- coding: Latin-1 -*-

n = 1       # num�ro de la case
g = 1       # nombre de grains � y d�poser
# Pour la variante, il suffit de d�finir g comme <float>
# en rempla�ant la ligne ci-dessus par :  g = 1.

while n < 65 :
    print n, g
    n, g = n+1, g*2
