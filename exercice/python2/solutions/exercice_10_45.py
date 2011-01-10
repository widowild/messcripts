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
    
dico ={}
while 1:
    choix = raw_input("Choisissez : (R)emplir - (C)onsulter - (T)erminer : ")
    if choix.upper() == 'T':
        break
    elif choix.upper() == 'R':
        remplissage()
    elif choix.upper() == 'C':
        consultation()
