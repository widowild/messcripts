#! /usr/bin/env python
# -*- coding:Utf-8 -*-

c = 1040                       # code du premier caractère (majuscule)
maju =""                       # chaîne destinée aux majuscules
minu =""                       # chaîne destinée aux minuscules
while c <1072:                 # on se limitera à cette gamme
    maju = maju + chr(c)
    minu = minu + chr(c +32)   # voir exercices précédents
    c = c+1
print(maju)
print(minu)
