# -*- coding:Utf8 -*-

import sys
from pg8000 import DBAPI
from dict_app import *

class GestionBD:
    "Mise en place et interfaçage d'une base de données PostgreSQL"
    def __init__(self, dbName, user, passwd, host, port =5432):
        "Établissement de la connexion - Création du curseur"
        try:
            self.baseDonn = DBAPI.connect(host =host, port =port,
                                          database =dbName,
                                          user=user, password=passwd)
        except Exception as err:
            print('La connexion avec la base de données a échoué :\n'\
                  'Erreur détectée :\n%s' % err)
            self.echec =1
        else:
            self.cursor = self.baseDonn.cursor()   # création du curseur
            self.echec =0

    def creerTables(self, dicTables):
        "Création des tables décrites dans le dictionnaire <dicTables>."
        for table in dicTables:            # parcours des clés du dictionn.
            req = "CREATE TABLE %s (" % table
            pk =''
            for descr in dicTables[table]:
                nomChamp = descr[0]        # libellé du champ à créer
                tch = descr[1]             # type de champ à créer
                if tch =='i':
                    typeChamp ='INTEGER'
                elif tch =='k':
                    # champ 'clé primaire' (entier incrémenté automatiquement)
                    typeChamp ='SERIAL'
                    pk = nomChamp
                else:
                    typeChamp ='VARCHAR(%s)' % tch
                req = req + "%s %s, " % (nomChamp, typeChamp)
            if pk == '':
                req = req[:-2] + ")"
            else:
                req = req + "CONSTRAINT %s_pk PRIMARY KEY(%s))" % (pk, pk)
            self.executerReq(req)

    def supprimerTables(self, dicTables):
        "Suppression de toutes les tables décrites dans <dicTables>"
        for table in list(dicTables.keys()):
            req ="DROP TABLE %s" % table
            self.executerReq(req)
        self.commit()                       # transfert -> disque

    def executerReq(self, req, param =None):
        "Exécution de la requête <req>, avec détection d'erreur éventuelle"
        try:
            self.cursor.execute(req, param)
        except Exception as err:
            # afficher la requête et le message d'erreur système :
            print("Requête SQL incorrecte :\n{}\nErreur détectée :".format(req))
            print(err)
            return 0
        else:
            return 1

    def resultatReq(self):
        "renvoie le résultat de la requête précédente (une liste de tuples)"
        return self.cursor.fetchall()

    def commit(self):
        if self.baseDonn:
            self.baseDonn.commit()         # transfert curseur -> disque

    def close(self):
        if self.baseDonn:
            self.baseDonn.close()

class Enregistreur:
    """classe pour gérer l'entrée d'enregistrements divers"""
    def __init__(self, bd, table):
        self.bd =bd
        self.table =table
        self.descriptif =Glob.dicoT[table]   # descriptif des champs

    def entrer(self):
        "procédure d'entrée d'un enregistrement entier"
        champs ="("           # ébauche de chaîne pour les noms de champs
        valeurs =[]           # liste pour les valeurs correspondantes
        # Demander successivement une valeur pour chaque champ :
        for cha, type, nom in self.descriptif:
            if type =="k":    # on ne demandera pas le n° d'enregistrement
                continue      # à l'utilisateur (numérotation auto.)
            champs = champs + cha + ","
            val = input("Entrez le champ %s :" % nom)
            if type =="i":
                val =int(val)
            valeurs.append(val)

        balises ="(" + "%s," * len(valeurs)       # balises de conversion
        champs = champs[:-1] + ")"    # supprimer la dernière virgule,
        balises = balises[:-1] + ")"  # et ajouter une parenthèse
        req ="INSERT INTO %s %s VALUES %s" % (self.table, champs, balises)
        self.bd.executerReq(req, valeurs)

        ch =input("Continuer (O/N) ? ")
        if ch.upper() == "O":
            return 0
        else:
            return 1

###### Programme principal : #########

# Création de l'objet-interface avec la base de données :
bd = GestionBD(Glob.dbName, Glob.user, Glob.passwd, Glob.host, Glob.port)
if bd.echec:
    sys.exit()

while 1:
    print("\nQue voulez-vous faire :\n"\
          "1) Créer les tables de la base de données\n"\
          "2) Supprimer les tables de la base de données ?\n"\
          "3) Entrer des compositeurs\n"\
          "4) Entrer des oeuvres\n"\
          "5) Lister les compositeurs\n"\
          "6) Lister les oeuvres\n"\
          "7) Exécuter une requête SQL quelconque\n"\
          "9) terminer ?                         Votre choix :", end=' ')
    ch = int(input())
    if ch ==1:
        # création de toutes les tables décrites dans le dictionnaire :
        bd.creerTables(Glob.dicoT)
    elif ch ==2:
        # suppression de toutes les tables décrites dans le dic. :
        bd.supprimerTables(Glob.dicoT)
    elif ch ==3 or ch ==4:
        # création d'un <enregistreur> de compositeurs ou d'oeuvres :
        table ={3:'compositeurs', 4:'oeuvres'}[ch]
        enreg =Enregistreur(bd, table)
        while 1:
            if enreg.entrer():
                break
    elif ch ==5 or ch ==6:
        # listage de tous les compositeurs, ou toutes les oeuvres :
        table ={5:'compositeurs', 6:'oeuvres'}[ch]
        if bd.executerReq("SELECT * FROM %s" % table):
            # analyser le résultat de la requête ci-dessus :
            records = bd.resultatReq()      # ce sera un tuple de tuples
            for rec in records:             # => chaque enregistrement
                for item in rec:            # => chaque champ dans l'enreg.
                    print(item, end=' ')
                print()
    elif ch ==7:
        req =input("Entrez la requête SQL : ")
        if bd.executerReq(req):
            print(bd.resultatReq())          # ce sera un tuple de tuples
    else:
        bd.commit()
        bd.close()
        break

