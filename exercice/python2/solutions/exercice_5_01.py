#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Conversion degr�s -> radians
# Rappel : un angle de 1 radian est un angle qui correspond � une portion
# de circonf�rence de longueur �gale � celle du rayon.
# Puisque la circonf�rence vaut 2 pi R, un angle de 1 radian correspond
# � 360� / 2 pi , ou encore � 180� / pi

# Angle fourni au d�part en degr�s, minutes, secondes :
deg, min, sec  = 32, 13, 49

# Conversion des secondes en une fraction de minute :
# (le point d�cimal force la conversion du r�sultat en un nombre r�el)
fm = sec/60.
# Conversion des minutes en une fraction de degr� :
fd = (min + fm)/60
# Valeur de l'angle en degr�s "d�cimalis�s" :
ang = deg + fd
# Valeur de pi :
pi = 3.14159265359
# Valeur d'un radian en degr�s :
rad = 180 / pi
# Conversion de l'angle en radians :
arad = ang / rad
# Affichage :
print deg, "�", min, "'", sec, '" =', arad, "radian(s)"
