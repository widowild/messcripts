#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Conversion �Fahrenheit <-> �Celsius

# A) Temp�rature fournie en �C :
tempC = 25
# Conversion en �Fahrenheit :
tempF = tempC * 1.8 + 32
# Affichage :
print tempC, "�C =", tempF, "�F"

# B) Temp�rature fournie en �F :
tempF = 25
# Conversion en �Celsius :
tempC = (tempF - 32) / 1.8
# Affichage :
print tempF, "�F =", tempC, "�C"
