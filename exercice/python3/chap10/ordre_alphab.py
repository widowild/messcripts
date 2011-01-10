#! /usr/bin/env python
# -*- coding: Utf8 -*-

while True:
    mot = input("Entrez un mot quelconque : (<enter> pour terminer)")
    if mot =="":
        break 
    if mot < "limonade":
        place = "précède"
    elif mot > "limonade":
        place = "suit"
    else:
        place = "se confond avec"
    print("Le mot", mot, place, "le mot 'limonade' dans l'ordre alphabétique")
