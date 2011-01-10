#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Cr�ation et Alimentation d'une petite base de donn�es

import gadfly
import os

chemin = os.getcwd()        # obtention du r�pertoire courant

connex = gadfly.gadfly()
connex.startup("musique", chemin)
cur = connex.cursor()
requete = "create table compositeurs (comp varchar, a_naiss integer,\
           a_mort integer)" 
cur.execute(requete)
requete = "create table oeuvres (comp varchar, titre varchar,\
           duree integer, interpr varchar)" 
cur.execute(requete)

print "Entr�e des enregistrements, table des compositeurs :"
while 1:
    nm = raw_input("Nom du compositeur (<Enter> pour terminer) : ")
    if nm =='':
        break
    an = raw_input("Ann�e de naissance : ")
    am = raw_input("Ann�e de mort : ")
    requete ="insert into compositeurs(comp, a_naiss, a_mort) values \
                 ('%s', %s, %s)" % (nm, an, am)
    cur.execute(requete)
# Affichage des donn�es entr�es, pour v�rification :
cur.execute("select * from compositeurs")
print cur.pp()

print "Entr�e des enregistrements, table des oeuvres musicales :"
while 1:
    nom = raw_input("Nom du compositeur (<Enter> pour terminer) : ")
    if nom =='':
        break
    tit = raw_input("Titre de l'oeuvre : ")
    dur = raw_input("dur�e (minutes) : ")
    int = raw_input("interpr�te principal : ")
    requete ="insert into oeuvres(comp, titre, duree, interpr) values \
                 ('%s', '%s', %s, '%s')" % (nom, tit, dur, int)
    cur.execute(requete)
# Affichage des donn�es entr�es, pour v�rification :
cur.execute("select * from oeuvres")
print cur.pp()

connex.commit()
