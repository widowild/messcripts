#! /usr/bin/env python
# -*- coding:Utf-8 -*-

def voyelle(cu):
    "teste si le caractère unicode <cu> est une voyelle"
    if cu in u"AEIOUYÀÉÈÊËÎÏÔÛÙaeiouyàéèêëîïôûù":
        return 1
    else:
        return 0

# Test :
if __name__ == '__main__':
    print voyelle(u"g"), voyelle(u"O"), voyelle(u"à"), voyelle(u"É")

