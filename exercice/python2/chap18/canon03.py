# -*- coding:Latin-1 -*-

#######################################################
# Jeu des bombardes - version monoposte - 2 joueurs   #
# (C) G�rard Swinnen, Verviers (Belgique) - July 2004 #
# Licence : GPL                                       #
#######################################################

from Tkinter import *
from math import sin, cos, pi
from random import randrange

class Canon:
    """Petit canon graphique"""
    def __init__(self, boss, id, x, y, sens, coul):
        self.boss = boss            # r�f. du canevas
        self.appli = boss.master    # r�f. de la fen�tre d'application 
        self.id = id                # identifiant du canon (cha�ne)
        self.coul = coul            # couleur associ�e au canon
        self.x1, self.y1 = x, y     # axe de rotation du canon
        self.sens = sens            # sens de tir (-1:gauche, +1:droite)
        self.lbu = 30               # longueur de la buse
        self.angle = 0              # hausse par d�faut (angle de tir)
        # retrouver la largeur et la hauteur du canevas :
        self.xMax = int(boss.cget('width'))
        self.yMax = int(boss.cget('height'))
        # dessiner la buse du canon (horizontale) :
        self.x2, self.y2 = x + self.lbu * sens, y
        self.buse = boss.create_line(self.x1, self.y1,
                                     self.x2, self.y2, width =10)
        # dessiner le corps du canon (cercle de couleur) :
        self.rc = 15                # rayon du cercle 
        self.corps = boss.create_oval(x -self.rc, y -self.rc, x +self.rc,
                                      y +self.rc, fill =coul)
        # pr�-dessiner un obus cach� (point en dehors du canevas) :
        self.obus = boss.create_oval(-10, -10, -10, -10, fill='red')
        self.anim = False           # indicateurs d'animation 
        self.explo = False          #    et d'explosion

    def orienter(self, angle):
        "r�gler la hausse du canon"
        # rem: le param�tre <angle> est re�u en tant que cha�ne.
        # Il faut donc le traduire en r�el, puis le convertir en radians :
        self.angle = float(angle)*pi/180
        # rem: utiliser la m�thode coords de pr�f�rence avec des entiers :       
        self.x2 = int(self.x1 + self.lbu * cos(self.angle) * self.sens)
        self.y2 = int(self.y1 - self.lbu * sin(self.angle))
        self.boss.coords(self.buse, self.x1, self.y1, self.x2, self.y2)
 
    def deplacer(self, x, y):
        "amener le canon dans une nouvelle position x, y"
        dx, dy = x -self.x1, y -self.y1     # valeur du d�placement
        self.boss.move(self.buse, dx, dy) 
        self.boss.move(self.corps, dx, dy)
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def feu(self):
        "tir d'un obus - seulement si le pr�c�dent a fini son vol"
        if not (self.anim or self.explo):
            self.anim =True
            # r�cup�rer la description de tous les canons pr�sents :
            self.guns = self.appli.dictionnaireCanons()
            # position de d�part de l'obus (c'est la bouche du canon) :
            self.boss.coords(self.obus, self.x2 -3, self.y2 -3,
                                        self.x2 +3, self.y2 +3)
            v = 17              # vitesse initiale
            # composantes verticale et horizontale de cette vitesse :
            self.vy = -v *sin(self.angle)
            self.vx = v *cos(self.angle) *self.sens
            self.animer_obus()
            return True     # => signaler que le coup est parti
        else:
            return False    # => le coup n'a pas pu �tre tir�

    def animer_obus(self):
        "animer l'obus (trajectoire balistique)"
        if self.anim:
            self.boss.move(self.obus, int(self.vx), int(self.vy))
            c = self.boss.coords(self.obus)     # coord. r�sultantes
            xo, yo = c[0] +3, c[1] +3      # coord. du centre de l'obus
            self.test_obstacle(xo, yo)     # a-t-on atteint un obstacle ?
            self.vy += .4                  # acc�l�ration verticale
            self.boss.after(20, self.animer_obus)
        else:
            # animation termin�e - cacher l'obus et d�placer les canons :
            self.fin_animation()
   
    def test_obstacle(self, xo, yo):
        "�valuer si l'obus a atteint une cible ou les limites du jeu"
        if yo >self.yMax or xo <0 or xo >self.xMax:
            self.anim =False
            return
        # analyser le dictionnaire des canons pour voir si les coord.
        # de l'un d'entre eux sont proches de celles de l'obus :
        for id in self.guns:              # id = clef dans dictionn.
            gun = self.guns[id]           # valeur correspondante
            if xo < gun.x1 +self.rc and xo > gun.x1 -self.rc \
            and yo < gun.y1 +self.rc and yo > gun.y1 -self.rc :
                self.anim =False
                # dessiner l'explosion de l'obus (cercle jaune) :
                self.explo = self.boss.create_oval(xo -12, yo -12,
                             xo +12, yo +12, fill ='yellow', width =0)
                self.hit =id       # r�f�rence de la cible touch�e
                self.boss.after(150, self.fin_explosion)
                break         
   
    def fin_explosion(self):
        "effacer l'explosion ; r�-initaliser l'obus ; g�rer le score"
        self.boss.delete(self.explo)    # effacer l'explosion
        self.explo =False               # autoriser un nouveau tir
        # signaler le succ�s � la fen�tre ma�tresse :
        self.appli.goal(self.id, self.hit)
        
    def fin_animation(self):
        "actions � accomplir lorsque l'obus a termin� sa trajectoire"
        self.appli.disperser()          # d�placer les canons
        # cacher l'obus (en l'exp�diant hors du canevas) :
        self.boss.coords(self.obus, -10, -10, -10, -10)


class Pupitre(Frame):
    """Pupitre de pointage associ� � un canon""" 
    def __init__(self, boss, canon):
        Frame.__init__(self, bd =3, relief =GROOVE)
        self.score =0
        self.appli =boss                # r�f. de l'application
        self.canon =canon               # r�f. du canon associ�
        # Syst�me de r�glage de l'angle de tir :
        self.regl =Scale(self, from_ =75, to =-15, troughcolor =canon.coul,
                         command =self.orienter)
        self.regl.set(45)               # angle initial de tir
        self.regl.pack(side =LEFT)
        # �tiquette d'identification du canon :
        Label(self, text =canon.id).pack(side =TOP, anchor =W, pady =5)
        # Bouton de tir :
        self.bTir =Button(self, text ='Feu !', command =self.tirer)
        self.bTir.pack(side =BOTTOM, padx =5, pady =5)
        Label(self, text ="points").pack()
        self.points =Label(self, text=' 0 ', bg ='white')
        self.points.pack()
        # positionner � gauche ou � droite suivant le sens du canon :
        if canon.sens == -1:
            self.pack(padx =5, pady =5, side =RIGHT)
        else:
            self.pack(padx =5, pady =5, side =LEFT)

    def tirer(self):
        "d�clencher le tir du canon associ�"
        self.canon.feu()
        
    def orienter(self, angle):
        "ajuster la hausse du canon associ�"
        self.canon.orienter(angle)

    def attribuerPoint(self, p):
        "incr�menter ou d�cr�menter le score, de <p> points"
        self.score += p
        self.points.config(text = ' %s ' % self.score)

class Application(Frame):
    '''Fen�tre principale de l'application'''
    def __init__(self):
        Frame.__init__(self)
        self.master.title('>>>>> Boum ! Boum ! <<<<<')
        self.pack()
        self.jeu = Canvas(self, width =400, height =250, bg ='ivory',
                          bd =3, relief =SUNKEN)
        self.jeu.pack(padx =8, pady =8, side =TOP)

        self.guns ={}           # dictionnaire des canons pr�sents
        self.pupi ={}           # dictionnaire des pupitres pr�sents
        # Instanciation de 2 'objets canons (+1, -1 = sens oppos�s) :
        self.guns["Billy"] = Canon(self.jeu, "Billy", 30, 200, 1, "red")
        self.guns["Linus"] = Canon(self.jeu, "Linus", 370,200,-1, "blue")
        # Instanciation de 2 pupitres de pointage associ�s � ces canons :
        self.pupi["Billy"] = Pupitre(self, self.guns["Billy"])
        self.pupi["Linus"] = Pupitre(self, self.guns["Linus"])

    def disperser(self):
        "d�placer al�atoirement les canons"
        for id in self.guns:
            gun =self.guns[id]
            # positionner � gauche ou � droite, suivant sens du canon :
            if gun.sens == -1 :
                x = randrange(320,380)
            else:
                x = randrange(20,80)
            # d�placement proprement dit :
            gun.deplacer(x, randrange(150,240))
  
    def goal(self, i, j):
        "le canon <i> signale qu'il a atteint l'adversaire <j>"
        if i != j:
            self.pupi[i].attribuerPoint(1)    
        else:
            self.pupi[i].attribuerPoint(-1)
            
    def dictionnaireCanons(self):
        "renvoyer le dictionnaire d�crivant les canons pr�sents" 
        return self.guns

if __name__ =='__main__':
    Application().mainloop()
