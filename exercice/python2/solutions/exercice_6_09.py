#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Ann�es bissextiles

print "Veuillez entrer l'ann�e � tester :",
a = input()

if a % 4 != 0:
    # a n'est pas divisible par 4 -> ann�e non bissextile
    bs = 0      
else:
    if a % 400 ==0:
        # a divisible par 400 -> ann�e bissextile
        bs = 1
    elif a % 100 ==0:
        # a divisible par 100 -> ann�e non bissextile
        bs = 0
    else:
        # autres cas ou a est divisible par 4 -> ann�e bissextile
        bs = 1
if bs ==1:
    ch = "est"
else:
    ch = "n'est pas"
print "L'ann�e", a, ch, "bissextile."

########### Variante (propos�e par Alex Misbah�) : #####

a = input('Veuillez entrer une ann�e :')

if (a%4==0) and ((a%100!=0) or (a%400==0)):
    print a,"est une ann�e bissextile"
else:
    print a,"n'est pas une ann�e bissextile"

