#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Table des codes ASCII

c = 32              # premier code ASCII <imprimable>

while c < 128 :     # dernier code strictement ASCII = 127 
    print "Code", c, ":", unichr(c), "  ",
    c = c + 1
