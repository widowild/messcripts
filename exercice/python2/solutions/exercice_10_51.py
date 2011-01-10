# -*- coding:Latin-1 -*-

def consultation():
    while 1:
        nom = raw_input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        if dico.has_key(nom):           # le nom est-il r�pertori� ?
            item = dico[nom]            # consultaion proprement dite
            age, taille = item[0], item[1]
            print "Nom : %s - �ge : %s ans - taille : %s m."\
                   % (nom, age, taille)          
        else:
            print "*** nom inconnu ! ***"

def remplissage():
    while 1:
        nom = raw_input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        age = int(raw_input("Entrez l'�ge (nombre entier !) : "))
        taille = float(raw_input("Entrez la taille (en m�tres) : "))
        dico[nom] = (age, taille)

def enregistrement():
    fich = raw_input("Entrez le nom du fichier de sauvegarde : ")
    ofi = open(fich, "w")
    # parcours du dictionnaire entier, converti au pr�alable en une liste :
    for cle, valeur in dico.items(): 
        # utilisation du formatage des cha�nes pour cr�er l'enregistrement :
        ofi.write("%s@%s#%s\n" % (cle, valeur[0], valeur[1]))
    ofi.close()

def lectureFichier():
    fich = raw_input("Entrez le nom du fichier de sauvegarde : ")
    try:
        ofi = open(fich, "r")
    except:
        print "*** fichier inexistant ***"
        return

    while 1:
        ligne = ofi.readline()
        if ligne =='':              # d�tection de la fin de fichier
            break
        enreg = ligne.split("@")    # restitution d'une liste [cl�,valeur]
        cle = enreg[0]
        valeur = enreg[1][:-1]      # �limination du caract�re de fin de ligne
        data = valeur.split("#")    # restitution d'une liste [�ge, taille]
        age, taille = int(data[0]), float(data[1])
        dico[cle] = (age, taille)   # reconstitution du dictionnaire
    ofi.close()

def sortie():
    print "*** Job termin� ***"
    return 1                        # afin de provoquer la sortie de la boucle 
    
def autre():
    print "Veuillez frapper R, A, C, S ou T, svp."
    
dico ={}
fonc ={"R":lectureFichier, "A":remplissage, "C":consultation,
       "S":enregistrement, "T":sortie}
while 1:
    choix = raw_input("Choisissez :\n" +\
    "(R)�cup�rer un dictionnaire pr�existant sauvegard� dans un fichier\n" +\
    "(A)jouter des donn�es au dictionnaire courant\n" +\
    "(C)onsulter le dictionnaire courant\n" +\
    "(S)auvegarder le dictionnaire courant dans un fichier\n" +\
    "(T)erminer : ")
    # l'instruction ci-dessous appelle une fonction diff�rente pour chaque
    # choix, par l'interm�diaire du dictionnaire <fonc> :
    if fonc.get(choix, autre)():
        break
    # note : toutes les fonctions appel�es ici renvoient <None> par d�faut
    #        sauf la fonction sortie() qui renvoie 1 => sortie de la boucle