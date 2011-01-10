#! /usr/bin/env python
# -*- coding:Utf8 -*-

from tkinter import *

class FunnyButton(Button):
    "Bouton de fantaisie : vert virant au rouge quand on l'actionne"
    def __init__(self, boss, **Arguments):
        Button.__init__(self, boss,  bg ="dark green", fg ="white", bd =5,
                        activebackground ="red", activeforeground ="yellow",
                        font =('Helvetica', 12, 'bold'), **Arguments)

class SpinBox(Frame):
    "widget composite comportant un Label et 2 boutons 'up' & 'down'"
    def __init__(self, boss, largC=5, largB =2, vList=[0], liInd=0, orient =Y):
        Frame.__init__(self, boss)
        self.vList =vList           # liste des valeurs à présenter
        self.liInd =liInd           # index de la valeur à montrer par défaut
        if orient ==Y:
            s, augm, dimi = TOP, "^", "v"      # Orientation 'verticale'
        else:
            s, augm, dimi = RIGHT, ">", "<"    # Orientation 'horizontale'
        Button(self, text =augm, width =largB, command =self.up).pack(side =s)
        self.champ = Label(self, bg ='white', width =largC,
                           text =str(vList[liInd]), relief =SUNKEN)
        self.champ.pack(pady =3, side =s)
        Button(self, text=dimi, width=largB, command =self.down).pack(side =s)

    def up(self):
        if self.liInd < len(self.vList) -1:
            self.liInd += 1
        else:
            self.bell()       # émission d'un bip
        self.champ.configure(text =str(self.vList[self.liInd]))

    def down(self):
        if self.liInd > 0:
            self.liInd -= 1
        else:
            self.bell()       # émission d'un bip
        self.champ.configure(text =str(self.vList[self.liInd]))

    def get(self):
        return self.vList[self.liInd]

class FenDessin(Toplevel):
    "Fenêtre satellite (modale) contenant un simple canevas"
    def __init__(self, **Arguments):
        Toplevel.__init__(self, **Arguments)
        self.geometry("250x200+100+240")
        self.overrideredirect(1)            # => fenêtre sans bordure ni bandeau
        self.transient(self.master)         # => fenêtre 'modale'
        self.can =Canvas(self, bg="ivory", width =200, height =150)
        self.img = PhotoImage(file ="papillon2.gif")
        self.can.create_image(90, 80, image =self.img)
        self.can.pack(padx =20, pady =20)

class FenControle(Toplevel):
    "Fenêtre satellite contenant des contrôles de redimensionnement"
    def __init__(self, boss, **Arguments):
        Toplevel.__init__(self, boss, **Arguments)
        self.geometry("250x200+400+230")
        self.resizable(width =0, height =0)    # => empêche le redimensionnement
        p =(10, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300)
        self.spX =SpinBox(self, largC=5,largB =1,vList =p,liInd=5,orient =X)
        self.spX.pack(pady =5)
        self.spY =SpinBox(self, largC=5,largB =1,vList =p,liInd=5,orient =Y)
        self.spY.pack(pady =5)
        FunnyButton(self, text ="Dimensionner le canevas",
                    command =boss.redimF1).pack(pady =5)

class Demo(Frame):
    "Démo. de quelques caractéristiques du widget Toplevel"
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("400x300+200+200")
        self.master.config(bg ="cadet blue")
        FunnyButton(self, text ="Top 1", command =self.top1).pack(side =LEFT)
        FunnyButton(self, text ="Top 2", command =self.top2).pack(side =LEFT)
        FunnyButton(self, text ="Quitter", command =self.quit).pack()
        self.pack(side =BOTTOM, padx =10, pady =10)

    def top1(self):
        self.fen1 =FenDessin(bg ="grey")

    def top2(self):
        self.fen2 =FenControle(self, bg ="khaki")

    def redimF1(self):
        dimX, dimY = self.fen2.spX.get(), self.fen2.spY.get()
        self.fen1.can.config(width =dimX, height =dimY)

if __name__ =="__main__":              # --- Programme de test ---
    Demo().mainloop()
