#! /usr/bin/env python
# -*- coding: Latin-1 -*-

from dessins_tortue import *

up()                        # relever le crayon
goto(-20, 120)              # positionner le point de d�part
tracer(0)                   # ne pas tra�nasser

# dessiner une s�rie de formes de + en + petites :
i, t = 0, 40
while i < 9:
    carre(t, 'red', 0)      # tracer un carr�
    forward(t + 5)          # avancer + loin
    etoile6(t, 'blue', 0)
    forward(t +5)           # avancer + loin
    triangle(t, 'red', 0)
    forward(t +5)           # avancer + loin
    etoile5(t, 'blue', 0)
    forward(t +5)           # avancer + loin

    t -= 3                  # diminuer la taille
    i = i +1

a = input()                 # attendre
