#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Instructions compos�es <while> - <if> - <elif> - <else>

print 'Choisissez un nombre de 1 � 3 (ou z�ro pour terminer) ',
a = input()
while a != 0:           # l'op�rateur != signifie "diff�rent de"
    if a == 1:
        print "Vous avez choisi un :"
        print "le premier, l'unique, l'unit� ..."
    elif a == 2:
        print "Vous pr�f�rez le deux :"
        print "la paire, le couple, le duo ..."
    elif a == 3:
        print "Vous optez pour le plus grand des trois :"
        print "le trio, la trinit�, le triplet ..."
    else :
        print "Un nombre entre UN et TROIS, s.v.p."
    print 'Choisissez un nombre de 1 � 3 (ou z�ro pour terminer) ',
    a = input()
print "Vous avez entr� z�ro :"
print "L'exercice est donc termin�."
