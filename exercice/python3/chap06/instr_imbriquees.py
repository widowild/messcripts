#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Instructions composées <while> - <if> - <elif> - <else>

print('Choisissez un nombre de 1 à 3 (ou zéro pour terminer) ', end=' ')
a = eval(input())       # traduit l'entrée en expression ( => un entier, ici)
while a:                # variante améliorée de : << while a != 0: >>
    if a == 1:
        print("Vous avez choisi un :")
        print("le premier, l'unique, l'unité ...")
    elif a == 2:
        print("Vous préférez le deux :")
        print("la paire, le couple, le duo ...")
    elif a == 3:
        print("Vous optez pour le plus grand des trois :")
        print("le trio, la trinité, le triplet ...")
    else :
        print("Un nombre entre UN et TROIS, s.v.p.")
    print('Choisissez un nombre de 1 à 3 (ou zéro pour terminer) ', end=' ')
    a = eval(input())
print("Vous avez entré zéro :")
print("L'exercice est donc terminé.")
