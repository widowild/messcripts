#! /usr/bin/env python2
# coding: Utf-8

##########################################################
###          Affichage et réglagle du volume.          ###
### Réalisé sous licence GNU GPL v3 par ArkSeth/Elzen. ###
##########################################################

import os, sys, gtk, time, signal, gobject, commands

class Volume:
    def __init__(self):
        self.win = gtk.Window(gtk.WINDOW_POPUP)
        #self.win.set_title("Visualisation du volume")
        self.win.parse_geometry("178x102+423+399")
        #self.win.set_property("skip-taskbar-hint", True)
        #self.win.set_property("skip-pager-hint", True)
        #self.win.set_property("accept-focus", False)
        #self.win.set_property("focus-on-map", False)
        self.win.connect("destroy", self.destroy)
        self.win.set_keep_above(True)
        self.win.set_decorated(False)
        self.win.stick()
        self.brd = gtk.Frame()
        self.brd.set_shadow_type(gtk.SHADOW_OUT)
        self.win.add(self.brd)
        self.box = gtk.VBox(False, 10)
        self.box.set_border_width(10)
        self.brd.add(self.box)
        self.img = gtk.Image()
        self.box.add(self.img)
        self.bar = gtk.ProgressBar()
        self.box.add(self.bar)
        self.glimpse()
    
    def glimpse(self):
        self.timer = time.time()+2
        gobject.timeout_add_seconds(2, self.delay)
        off = commands.getoutput("amixer get Master | cut -d'\n' -f5 | grep off")
        theme = gtk.icon_theme_get_default()
        if off == "":
            vol = int(commands.getoutput("amixer get Master | cut -d'\n' -f5 | cut -d'[' -f2 | cut -d'%' -f1"))
            if vol == 0:
                self.img.set_from_pixbuf(theme.load_icon("audio-volume-zero", 48, gtk.ICON_LOOKUP_USE_BUILTIN))
                self.bar.set_fraction(0)
            elif vol < 34:
                self.img.set_from_pixbuf(theme.load_icon("audio-volume-low", 48, gtk.ICON_LOOKUP_USE_BUILTIN))
                self.bar.set_fraction(vol/100.0)
            elif vol > 66:
                self.img.set_from_pixbuf(theme.load_icon("audio-volume-high", 48, gtk.ICON_LOOKUP_USE_BUILTIN))
                self.bar.set_fraction(vol/100.0)
            else:
                self.img.set_from_pixbuf(theme.load_icon("audio-volume-medium", 48, gtk.ICON_LOOKUP_USE_BUILTIN))
                self.bar.set_fraction(vol/100.0)
        else:
            self.img.set_from_pixbuf(theme.load_icon("audio-volume-muted", 48, gtk.ICON_LOOKUP_USE_BUILTIN))
            self.bar.set_fraction(0)
    
    def destroy(self, widget, data=None):
        gtk.main_quit()
    
    def delay(self):
        if self.timer < time.time():
            gtk.main_quit()
        return True
    
    def handler(self, signum, frame):
        self.glimpse()
    
    def main(self):
        signal.signal(signal.SIGUSR1, self.handler)
        gobject.timeout_add_seconds(2, self.delay)
        self.img.show()
        self.bar.show()
        self.box.show()
        self.brd.show()
        self.win.show()
        gtk.main()

if len(sys.argv) != 2:
    quit()

if sys.argv[1] == "up":
    os.system("amixer -q set Master 5%+")

if sys.argv[1] == "down":
    os.system("amixer -q set Master 5%-")

if sys.argv[1] == "toggle":
    os.system("amixer -q set Master toggle")

pids = commands.getoutput('ps -ef -U $USER | grep -v grep | grep "'+sys.argv[0]+'" | tr -s " " | cut -d" " -f2').split("\n")
if (len(pids) > 1):
    for pid in pids: os.system('kill -s USR1 '+pid)
else: Volume().main()
