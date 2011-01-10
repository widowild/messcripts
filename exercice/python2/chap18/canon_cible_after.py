# -*- coding:Latin-1 -*-

#####################################
# Bombardement d'une cible mobile   #
# (C) G. Swinnen - Avril 2004 - GPL #
#####################################

from Tkinter import *
from math import sin, cos, pi
from random import randrange
from threading import Thread

class Canon:
    """Petit canon graphique"""
    def __init__(self, boss, num, x, y, sens):
        self.boss = boss            # r�f�rence du canevas
        self.num = num              # n� du canon dans la liste
        self.x1, self.y1 = x, y     # axe de rotation du canon
        self.sens = sens            # sens de tir (-1:gauche, +1:droite)
        self.lbu = 30               # longueur de la buse
        # dessiner la buse du canon (horizontale) :
        self.x2, self.y2 = x + self.lbu * sens, y
        self.buse = boss.create_line(self.x1, self.y1,
                                     self.x2, self.y2, width =10)
        # dessiner le corps du canon (cercle de couleur) :
        self.rc = 15                # rayon du cercle 
        self.corps = boss.create_oval(x -self.rc, y -self.rc, x +self.rc,
                                      y +self.rc, fill ='black')
        # pr�-dessiner un obus (au d�part c'est un simple point) :
        self.obus = boss.create_oval(x, y, x, y, fill='red')
        self.anim = 0
        # retrouver la largeur et la hauteur du canevas :
        self.xMax = int(boss.cget('width'))
        self.yMax = int(boss.cget('height'))

    def orienter(self, angle):
        "r�gler la hausse du canon"
        # rem : le param�tre <angle> est re�u en tant que cha�ne.
        # il faut donc le traduire en r�el, puis le convertir en radians :
        self.angle = float(angle)*2*pi/360      
        self.x2 = self.x1 + self.lbu * cos(self.angle) * self.sens
        self.y2 = self.y1 - self.lbu * sin(self.angle)
        self.boss.coords(self.buse, self.x1, self.y1, self.x2, self.y2)
        
    def feu(self):
        "d�clencher le tir d'un obus"
        # r�f�rence de l'objet cible :
        self.cible = self.boss.master.cible
        if self.anim ==0:
            self.anim =1
            # position de d�part de l'obus (c'est la bouche du canon) :
            self.xo, self.yo = self.x2, self.y2
            v = 20              # vitesse initiale
            # composantes verticale et horizontale de cette vitesse :
            self.vy = -v *sin(self.angle)
            self.vx = v *cos(self.angle) *self.sens
            self.animer_obus()
    
    def animer_obus(self):
        "animer l'obus (trajectoire balistique)"
        # positionner l'obus, en re-d�finissant ses coordonn�es :
        self.boss.coords(self.obus, self.xo -3, self.yo -3,
                                    self.xo +3, self.yo +3)
        if self.anim >0:
            # calculer la position suivante :
            self.xo += self.vx
            self.yo += self.vy
            self.vy += .5
            self.test_obstacle()        # a-t-on atteint un obstacle ?
            self.boss.after(15, self.animer_obus)
        else:
            # fin de l'animation :
            self.boss.coords(self.obus, self.x1, self.y1, self.x1, self.y1) 
   
    def test_obstacle(self):
        "�valuer si l'obus a atteint une cible ou les limites du jeu"
        if self.yo >self.yMax or self.xo <0 or self.xo >self.xMax:
            self.anim =0
            return
        if self.yo > self.cible.y -3 and self.yo < self.cible.y +18 \
        and self.xo > self.cible.x -3 and self.xo < self.cible.x +43:
            # dessiner l'explosion de l'obus (cercle orange) :
            self.explo = self.boss.create_oval(self.xo -10,
                         self.yo -10, self.xo +10, self.yo +10,
                         fill ='orange', width =0)
            self.boss.after(150, self.fin_explosion)
            self.anim =0
   
    def fin_explosion(self):
        "effacer le cercle d'explosion - g�rer le score"
        self.boss.delete(self.explo)
        # signaler le succ�s � la fen�tre ma�tresse :
        self.boss.master.goal()        

class Pupitre(Frame):
    """Pupitre de pointage associ� � un canon""" 
    def __init__(self, boss, canon):
        Frame.__init__(self, bd =3, relief =GROOVE)
        self.score =0
        s =Scale(self, from_ =88, to =65,
                 troughcolor ='dark grey',
                 command =canon.orienter)
        s.set(45)                       # angle initial de tir
        s.pack(side =LEFT)
        Label(self, text ='Hausse').pack(side =TOP, anchor =W, pady =5)        
        Button(self, text ='Feu !', command =canon.feu).\
                                    pack(side =BOTTOM, padx =5, pady =5)
        Label(self, text ="points").pack()
        self.points =Label(self, text=' 0 ', bg ='white')
        self.points.pack()
        # positionner � gauche ou � droite suivant le sens du canon :
        gd =(LEFT, RIGHT)[canon.sens == -1]
        self.pack(padx =3, pady =5, side =gd)

    def attribuerPoint(self, p):
        "incr�menter ou d�cr�menter le score"
        self.score += p
        self.points.config(text = ' %s ' % self.score)

class Cible:
    """objet graphique servant de cible"""
    def __init__(self, can, x, y):
        self.can = can             # r�f�rence du canevas
        self.x, self.y = x, y
        self.cible = can.create_oval(x, y, x+40, y+15, fill ='purple')
        
    def deplacer(self, dx, dy):
        "effectuer avec la cible un d�placement dx,dy" 
        self.can.move(self.cible, dx, dy)
        self.x += dx
        self.y += dy
        return self.x, self.y

class Thread_cible(Thread):
    """objet thread g�rant l'animation de la cible"""
    def __init__(self, app, cible):
        Thread.__init__(self)
        self.cible = cible          # objet � d�placer
        self.app = app              # r�f. de la fen�tre d'application
        self.sx, self.sy = 6, 3     # incr�ments d'espace et de
        self.dt =300                # temps pour l'animation (ms)
   
    def run(self):
        "animation, tant que la fen�tre d'application existe" 
        x, y = self.cible.deplacer(self.sx, self.sy)
        if x > self.app.xm -50 or x < self.app.xm /5:
                self.sx = -self.sx
        if y < self.app.ym /2 or y > self.app.ym -20:
                self.sy = -self.sy
        if self.app != None:
            self.app.after(int(self.dt), self.run)

    def stop(self):
        "fermer le thread si la fen�tre d'application est referm�e"
        self.app =None
        
    def accelere(self):
        "acc�l�rer le mouvement"
        self.dt /= 1.5
        self.app.bell()

class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('<<< Tir sur cible mobile >>>')
        self.pack()
        self.xm, self.ym = 600, 500
        self.jeu = Canvas(self, width =self.xm, height =self.ym,
                          bg ='ivory', bd =3, relief =SUNKEN)
        self.jeu.pack(padx =4, pady =4, side =TOP)

        # Instanciation d'un canon et d'un pupitre de pointage :
        x, y = 30, self.ym -20
        self.gun =Canon(self.jeu, 1, x, y, 1)
        self.pup =Pupitre(self, self.gun)
        
        # instanciation de la cible mobile :
        self.cible = Cible(self.jeu, self.xm/2, self.ym -25)
        # animation de la cible mobile, sur son propre thread :
        self.tc = Thread_cible(self, self.cible)
        self.tc.start()
        # arr�ter tous les threads lorsque l'on ferme la fen�tre :
        self.bind('<Destroy>',self.fermer_threads)

    def goal(self):
        "la cible a �t� touch�e"
        self.pup.attribuerPoint(1)
        self.tc.accelere()
        
    def fermer_threads(self, evt):
        "arr�ter le thread d'animation de la cible"
        self.tc.stop()

if __name__ =='__main__':
    Application().mainloop()
