# -*- coding:Utf8 -*-

# Mini-système de base de données

def consultation():
    while 1:
        nom = input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        if nom in dico:                 # le nom est-il répertorié ?
            item = dico[nom]            # consultaion proprement dite
            age, taille = item[0], item[1]
            print("Nom : {} - âge : {} ans - taille : {} m.".\
                  format(nom, age, taille))
        else:
            print("*** nom inconnu ! ***")

def remplissage():
    while 1:
        nom = input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        age = int(input("Entrez l'âge (nombre entier !) : "))
        taille = float(input("Entrez la taille (en mètres) : "))
        dico[nom] = (age, taille)

def enregistrement():
    fich = input("Entrez le nom du fichier de sauvegarde : ")
    ofi = open(fich, "w")
    # écriture d'une ligne-repère pour identifier le type de fichier :
    ofi.write("DicoExercice10.50\n")
    # parcours du dictionnaire entier, converti au préalable en une liste :
    for cle, valeur in list(dico.items()):
        # utilisation du formatage des chaînes pour créer l'enregistrement :
        ofi.write("{}@{}#{}\n".format(cle, valeur[0], valeur[1]))
    ofi.close()

def lectureFichier():
    fich = input("Entrez le nom du fichier de sauvegarde : ")
    try:
        ofi = open(fich, "r")
    except:
        print("*** fichier inexistant ***")
        return
    # Vérification : le fichier est-il bien de notre type spécifique ? :
    repere =ofi.readline()
    if repere != "DicoExercice10.50\n":
        print("*** type de fichier incorrect ***")
        return
    # Lecture des lignes restantes du fichier :
    while 1:
        ligne = ofi.readline()
        if ligne =='':              # détection de la fin de fichier
            break
        enreg = ligne.split("@")    # restitution d'une liste [clé,valeur]
        cle = enreg[0]
        valeur = enreg[1][:-1]      # élimination du caractère de fin de ligne
        data = valeur.split("#")    # restitution d'une liste [âge, taille]
        age, taille = int(data[0]), float(data[1])
        dico[cle] = (age, taille)   # reconstitution du dictionnaire
    ofi.close()

def sortie():
    print("*** Job terminé ***")
    return 1                        # afin de provoquer la sortie de la boucle

def autre():
    print("Veuillez frapper R, A, C, S ou T, svp.")

######## * Programme principal * #########

dico ={}
fonc ={"R":lectureFichier, "A":remplissage, "C":consultation,
       "S":enregistrement, "T":sortie}
while 1:
    choix = input("Choisissez :\n" +\
    "(R)écupérer un dictionnaire préexistant sauvegardé dans un fichier\n" +\
    "(A)jouter des données au dictionnaire courant\n" +\
    "(C)onsulter le dictionnaire courant\n" +\
    "(S)auvegarder le dictionnaire courant dans un fichier\n" +\
    "(T)erminer : ").upper()
    # l'instruction ci-dessous appelle une fonction différente pour chaque
    # choix, par l'intermédiaire du dictionnaire <fonc> :
    if fonc.get(choix, autre)():
        break
    # note : toutes les fonctions appelées ici renvoient <None> par défaut
    #        sauf la fonction sortie() qui renvoie 1 => sortie de la boucle
