#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Traitement de nombres entiers compris entre deux limites

print "Veuillez entrer la limite inf�rieure :",
a = input()
print "Veuillez entrer la limite sup�rieure :",
b = input()
s = 0                   # somme recherch�e (nulle au d�part)
# Parcours de la s�rie des nombres compris entre a et b :
n = a                   # nombre en cours de traitement
while n <= b:
    if n % 3 ==0 and n % 5 ==0:      # variante : 'or' au lieu de 'and'
        s = s + n
    n = n + 1

print "La somme recherch�e vaut", s
