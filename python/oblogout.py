#!/usr/bin/env python3
# -*- coding:utf8 -*-
#=================
# Dependance:
# python, tk, dbus, openbox

from tkinter import *
import os
import subprocess

# Logout
def logout():
    pid1 = subprocess.Popen("openbox --exit", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).pid
    fen1.destroy()
    print('résultat:', pid1)
# Reboot
def reboot():
    pid2 = subprocess.Popen('dbus-send --system --print-reply --dest="org.freedesktop.ConsoleKit" /org/freedesktop/ConsoleKit/Manager org.freedesktop.ConsoleKit.Manager.Restart', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).pid
    print('résultat:', pid2)
    fen1.destroy()

# Shutdown
def shutdown():
    pid3 = subprocess.Popen('dbus-send --system --print-reply --dest="org.freedesktop.ConsoleKit" /org/freedesktop/ConsoleKit/Manager org.freedesktop.ConsoleKit.Manager.Stop', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).pid
    print('résultat:', pid3)

# Suspend
def suspend():
    pid4 = subprocess.Popen('dbus-send --system --print-reply --dest="org.freedesktop.UPower" /org/freedesktop/UPower org.freedesktop.UPower.Suspend', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).pid
    print('résultat:', pid4)
    fen1.destroy()

fen1 = Tk()
fen1.title("Openbox")
fen1.maxsize(width=400, height=60)
fen1.minsize(width=150, height=30)
fen1.resizable(width=YES, height=NO)
bou1 = Button(fen1, text='Eteindre', command=shutdown)
bou1.pack(side=LEFT)
bou2 = Button(fen1, text='Redémarrer', command=reboot)
bou2.pack(side=LEFT)
bou3 = Button(fen1, text='Logout', command=logout)
bou3.pack(side=LEFT)
bou4 = Button(fen1, text='Suspendre', command=suspend)
bou4.pack(side=LEFT)
bou5 = Button(fen1, text='Annuler', command=fen1.quit)
bou5.pack(side=LEFT)
fen1.mainloop()
fen1.destroy()
