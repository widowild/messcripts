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
    pid2 = subprocess.Popen('dbus-send --system --print-reply --dest="org.freedesktop.Hal" /org/freedesktop/Hal/devices/computer org.freedesktop.Hal.Device.SystemPowerManagement.Reboot', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).pid
    print('résultat:', pid2)
    fen1.destroy()

# Shutdown
def shutdown():
    pid3 = subprocess.Popen('dbus-send --system --print-reply --dest="org.freedesktop.Hal" /org/freedesktop/Hal/devices/computer org.freedesktop.Hal.Device.SystemPowerManagement.Shutdown', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).pid
    print('résultat:', pid3)
    fen1.destroy()

fen1 = Tk()
fen1.title("Openbox")
fen1.maxsize(width=300, height=60)
fen1.minsize(width=150, height=30)
fen1.resizable(width=YES, height=NO)
bou1 = Button(fen1, text='Eteindre', command=shutdown)
bou1.pack(side=LEFT)
bou2 = Button(fen1, text='Redémarrer', command=reboot)
bou2.pack(side=LEFT)
bou3 = Button(fen1, text='Logout', command=logout)
bou3.pack(side=LEFT)
bou4 = Button(fen1, text='Annuler', command=fen1.quit)
bou4.pack(side=LEFT)
fen1.mainloop()
fen1.destroy()
