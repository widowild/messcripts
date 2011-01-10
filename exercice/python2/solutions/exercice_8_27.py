#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Chutes et rebonds

from Tkinter import *

def move():
    global x, y, v, dx, dv, flag
    xp, yp = x, y            # m�morisation des coord. pr�c�dentes
    # d�placement horizontal :
    if x > 385 or x < 15 :   # rebond sur les parois lat�rales :
        dx = -dx             # on inverse le d�placement
    x = x + dx
    # variation de la vitesse verticale (toujours vers le bas):
    v = v + dv
    # d�placement vertical (proportionnel � la vitesse)
    y = y + v       
    if y > 240:              # niveau du sol � 240 pixels : 
        y = 240              #  d�fense d'aller + loin !
        v = -v               # rebond : la vitesse s'inverse
    # on repositionne la balle :    
    can.coords(balle, x-10, y-10, x+10, y+10)
    # on trace un bout de trajectoire :
    can.create_line(xp, yp, x, y, fill ='light grey')
    # ... et on remet �a jusqu'� plus soif :
    if flag > 0:
        fen.after(50,move)

def start():
    global flag
    flag = flag +1
    if flag == 1:
        move()

def stop():
    global flag
    flag =0

# initialisation des coordonn�es, des vitesses et du t�moin d'animation :    
x, y, v, dx, dv, flag  = 15, 15, 0, 6, 5, 0

fen = Tk()
fen.title(' Chutes et rebonds')
can = Canvas(fen, width =400, height=250, bg="white")
can.pack()
balle = can.create_oval(x-10, y-10, x+10, y+10, fill='red')
Button(fen, text='Start', command =start).pack(side =LEFT, padx =10)
Button(fen, text='Stop', command =stop).pack(side =LEFT)
Button(fen, text='Quitter', command =fen.quit).pack(side =RIGHT, padx =10)

fen.mainloop()
