# -*- coding: Latin-1 -*-

#######################################################
# Jeu des bombardes - partie cliente                  #
# (C) G�rard Swinnen, Li�ge (Belgique) - Juillet 2004 #
# Licence : GPL                                       #
# Avant d'ex�cuter ce script, v�rifiez que l'adresse, #
# le num�ro de port et les dimensions de l'espace de  #
# jeu indiqu�es ci-dessous correspondent exactement   #
# � ce qui a �t� d�fini pour le serveur.              #
#######################################################

from Tkinter import *
import socket, sys, threading, time
from canon_serveur import Canon, Pupitre, AppServeur 

host, port = '192.168.0.235', 35000
largeur, hauteur = 700, 400          # dimensions de l'espace de jeu

class AppClient(AppServeur):
    def __init__(self, host, port, larg_c, haut_c):
        AppServeur.__init__(self, host, port, larg_c, haut_c)
        
    def specificites(self):
        "pr�parer les objets sp�cifiques de la partie client"    
        self.master.title('<<< Jeu des bombardes >>>')
        self.connex =ThreadSocket(self, self.host, self.port)
        self.connex.start()
        self.id =None

    def ajouter_canon(self, id, x, y, sens, coul):
        "instancier un canon et un pupitre de nom <id> dans 2 dictionnaires"
        self.guns[id] = Canon(self.jeu, id, int(x), int(y), int(sens), coul)
        self.pupi[id] = Pupitre(self, self.guns[id])
        self.pupi[id].inactiver()
    
    def activer_pupitre_personnel(self, id):
        self.id =id                         # identifiant re�u du serveur
        self.pupi[id].activer()
        
    def tir_canon(self, id):
        r = self.guns[id].feu()             # renvoie False si enray�
        if r and id == self.id:
            self.connex.signaler_tir()
        
    def imposer_score(self, id, sc):
        self.pupi[id].valeur_score(int(sc))
        
    def deplacer_canon(self, id, x, y):
        "note: les valeurs de x et y sont re�ues en tant que cha�nes"
        self.guns[id].deplacer(int(x), int(y))

    def orienter_canon(self, id, angle):
        "r�gler la hausse du canon <id> � la valeur <angle>"
        self.guns[id].orienter(angle)
        if id == self.id:
            self.connex.signaler_angle(angle)
        else:
            self.pupi[id].reglage(angle)
            
    def fermer_threads(self, evt):
        "couper les connexions existantes et refermer les threads"
        self.connex.terminer()
        self.active =0                  # emp�cher acc�s ult�rieurs � Tk

    def depl_aleat_canon(self, id):
        pass                            # => m�thode inop�rante

    def goal(self, a, b):
        pass                            # => m�thode inop�rante


class ThreadSocket(threading.Thread):
    """objet thread g�rant l'�change de messages avec le serveur"""
    def __init__(self, boss, host, port):
        threading.Thread.__init__(self)
        self.app = boss            # r�f. de la fen�tre application
        # Mise en place du socket - connexion avec le serveur :
        self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connexion.connect((host, port))
        except socket.error:
            print "La connexion a �chou�."
            sys.exit()    
        print "Connexion �tablie avec le serveur."

    def run(self):
        while 1:
            msg_recu = self.connexion.recv(1024)
            print "*%s*" % msg_recu
            # le message re�u est d'abord converti en une liste :
            t =msg_recu.split(',')
            if t[0] =="" or t[0] =="fin":
                # fermer le pr�sent thread :
                break                   
            elif t[0] =="serveur OK":
                self.connexion.send("client OK")
            elif t[0] =="canons":
                self.connexion.send("OK")       # accus� de r�ception
                # �liminons le 1er et le dernier �l�ment de la liste.
                # ceux qui restent sont eux-m�mes des listes :
                lc = t[1:-1]
                # chacune est la description compl�te d'un canon :
                for g in lc:
                    s = g.split(';')
                    self.app.ajouter_canon(s[0], s[1], s[2], s[3], s[4])
            elif t[0] =="nouveau_canon":
                self.app.ajouter_canon(t[1], t[2], t[3], t[4], t[5])
                if len(t) >6:
                    self.app.activer_pupitre_personnel(t[1])
            elif t[0] =='angle':
                # il se peut que l'on ait re�u plusieurs infos regroup�es.
                # on ne consid�re alors que la premi�re :
                self.app.orienter_canon(t[1], t[2])                 
            elif t[0] =="tir_de":
                self.app.tir_canon(t[1])
            elif t[0] =="scores":
                # �liminons le 1er et le dernier �l�ment de la liste.
                # ceux qui restent sont eux-m�mes des listes :
                lc = t[1:-1]
                # chaque �l�ment est la description d'un score :
                for g in lc:
                    s = g.split(';')
                    self.app.imposer_score(s[0], s[1])
            elif t[0] =="mouvement_de":
                self.app.deplacer_canon(t[1],t[2],t[3])
            elif t[0] =="d�part_de":
                self.app.enlever_canon(t[1])

        # Le thread <r�ception> se termine ici.
        print "Client arr�t�. Connexion interrompue."
        self.connexion.close()
        
    def signaler_tir(self):
        self.connexion.send('feu')

    def signaler_angle(self, angle):
        self.connexion.send('orienter,%s,' % angle)
    
    def terminer(self):
        self.connexion.send('fin')

# Programme principal :
if __name__ =='__main__':
    AppClient(host, port, largeur, hauteur).mainloop()            
