#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Création et Alimentation d'une petite base de données SQLite

import sqlite3

# Établissement de la connexion - Création du curseur :
connex = sqlite3.connect("musique.sq3")
cur = connex.cursor()
# Création des tables. L'utilisation de try/except permet de ré-utiliser le
# script indéfiniment, même si la base de données existe déjà.
try:
    req ="CREATE TABLE compositeurs(comp TEXT, a_naiss INTEGER, a_mort INTEGER)"
    cur.execute(req)
    req ="CREATE TABLE oeuvres(comp TEXT,titre TEXT,duree INTEGER,interpr TEXT)"
    cur.execute(req)
except:
    pass                # Les tables existent certainement déjà => on continue.

print("Entrée des enregistrements, table des compositeurs :")
while 1:
    nom = input("Nom du compositeur (<Enter> pour terminer) : ")
    if nom =='':
        break
    aNais = input("Année de naissance : ")
    aMort = input("Année de mort : ")
    req ="INSERT INTO compositeurs (comp, a_naiss, a_mort) VALUES (?, ?, ?)"
    cur.execute(req, (nom, aNais, aMort))

print("Rappel des infos introduites :")
cur.execute("select * from compositeurs")
for enreg in cur:
    print(enreg)

print("Entrée des enregistrements, table des oeuvres musicales :")
while 1:
    nom = input("Nom du compositeur (<Enter> pour terminer) : ")
    if nom =='':
        break
    titre = input("Titre de l'oeuvre : ")
    duree = input("durée (minutes) : ")
    inter = input("interprète principal : ")
    req ="INSERT INTO oeuvres (comp, titre, duree, interpr) VALUES (?, ?, ?, ?)"
    cur.execute(req, (nom, titre, duree, inter))

print("Rappel des infos introduites :")
cur.execute("select * from oeuvres")
for enreg in cur:
    print(enreg)

# Transfert effectif des enregistrements dans la BD :
connex.commit()
