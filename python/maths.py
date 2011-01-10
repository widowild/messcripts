#!/usr/bin/env python3
# -*- coding:Utf8 -*-
#=================
from math import *
# identite remarquable
print("Identité remarquable")
print("(a-b)2 = a2-2ab+b2")
va = input("Veuillez donner une valeur pour a: ")
a = int(va)
print("Valeur de a =", a)
vb = input("Veuillez donner une valeur pour b: ")
b= int(vb)
print("Valeur de b =", b)
print("(",a,"-",b,")^2", "=",a**2,"-",2*a*b,"+",b**2)
print("(",a,"-",b,")^2", "=",(a**2) - (2*a*b) + (b**2))
