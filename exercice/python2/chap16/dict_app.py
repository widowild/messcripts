# -*- coding:Latin-1 -*-

class Glob:
    """Espace de noms pour les variables et fonctions <pseudo-globales>"""

    dbName = "discotheque"      # nom de la base de donn�es
    user = "jules"              # propri�taire ou utilisateur
    passwd = "abcde"            # mot de passe d'acc�s
    host = "192.168.0.235"      # nom ou adresse IP du serveur

    # Structure de la base de donn�es.  Dictionnaire des tables & champs :
    dicoT ={"compositeurs":[('id_comp', "k", "cl� primaire"),
                            ('nom', 25, "nom"),
                            ('prenom', 25, "pr�nom"),
                            ('a_naiss', "i", "ann�e de naissance"),
                            ('a_mort', "i", "ann�e de mort")],
            "oeuvres":[('id_oeuv', "k", "cl� primaire"),
                       ('id_comp', "i", "cl� compositeur"),
                       ('titre', 50, "titre de l'oeuvre"),
                       ('duree', "i", "dur�e (en minutes)"),
                       ('interpr', 30, "interpr�te principal")]}

