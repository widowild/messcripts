#! /usr/bin/env python
# -*- coding: Utf8 -*-

# Traitement et conversion de lignes dans un fichier texte

def traiteLigne(ligne):
    "remplacement des espaces de la ligne de texte par '-*-' "
    newLine =""                      # nouvelle chaîne à construire
    c, m = 0, 0                      # initialisations
    while c < len(ligne):            # lire tous les caractères de la ligne
        if ligne[c] == " ":          
            # Le caractère lu est un espace.
            # On ajoute une 'tranche' à la chaîne en cours de construction :
            newLine = newLine + ligne[m:c] + "-*-"
            # On mémorise dans m la position atteinte dans la ligne lue :
            m = c + 1                # ajouter 1 pour "oublier" l'espace
        c = c + 1
    # Ne pas oublier d'ajouter la 'tranche' suivant le dernier espace :
    newLine = newLine + ligne[m:]
    # Renvoyer la chaîne construite :
    return newLine

# --- Programme principal : ---
nomFS = input("Nom du fichier source (Latin-1) : ")
nomFD = input("Nom du fichier destinataire (Utf-8) : ")
fs = open(nomFS, 'r', encoding ="Latin1")    # ouverture des 2 fichiers
fd = open(nomFD, 'w', encoding ="Utf8")      # dans les encodages spécifiés
while 1:                            # boucle de traitement
    li = fs.readline()              # lecture d'une ligne
    if li == "":                    # détection de la fin du fichier :
        break                       # readline() renvoie une chaîne vide
    fd.write(traiteLigne(li))       # traitement + écriture   
fd.close()
fs.close()

