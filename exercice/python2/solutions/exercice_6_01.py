#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Conversion de miles/heure en km/h et m/s

print "Veuillez entrer le nombre de miles parcourus en une heure : ",
ch = raw_input()            # en g�n�ral pr�f�rable � input()
mph = float(ch)             # conversion de la cha�ne entr�e en nombre r�el
mps = mph * 1609 / 3600     # conversion en m�tres par seconde
kmph = mph * 1.609          # conversion en km/h

# affichage :
print mph, "miles/heure =", kmph, "km/h, ou encore", mps, "m/s"
