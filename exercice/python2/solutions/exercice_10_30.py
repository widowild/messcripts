#! /usr/bin/env python
# -*- coding:Utf-8 -*-

lst = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne',
       'Maximilien', 'Alexandre-Benoît', 'Louise']

for e in lst:
     # Le comptage des caractères n'est garanti correct qu'en unicode :
     print "%s : %s caractères" % (e, len(e.decode("Utf8")))
