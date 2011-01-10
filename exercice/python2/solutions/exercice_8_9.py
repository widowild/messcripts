# -*- coding:Latin-1 -*-

# Dessin d'un damier
 
from Tkinter import *

def damier():
    "dessiner dix lignes de carr�s avec d�calage altern�"
    y = 0
    while y < 10:
        if y % 2 == 0:              # une fois sur deux, on
            x = 0                   # commencera la ligne de
        else:                       # carr�s avec un d�calage
            x = 1                   # de la taille d'un carr�
        ligne_de_carres(x*c, y*c)
        y += 1
        
def ligne_de_carres(x, y):
    "dessiner une ligne de carr�s, en partant de x, y" 
    i = 0
    while i < 10:
        can.create_rectangle(x, y, x+c, y+c, fill='navy')
        i += 1
        x += c*2                    # espacer les carr�s
        
##### Programme principal : ############
    
# T�chez de bien "param�trer" vos programmes, comme nous l'avons
# fait dans ce script. Celui-ci peut en effet tracer des damiers
# de n'importe quelle taille, en changeant seulement la valeur
# d'une seule variable, � savoir la dimension des carr�s :

c = 30                  # taille des carr�s

fen = Tk()
can = Canvas(fen, width =c*10, height =c*10, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(fen, text ='damier', command =damier)
b1.pack(side =LEFT, padx =3, pady =3)
fen.mainloop()