#! /usr/bin/env python
# -*- coding:Utf-8 -*-

def voyelle(car):
    "teste si le caractère <car> est une voyelle"
    if car in "AEIOUYÀÉÈÊËÎÏÔÛÙaeiouyàéèêëîïôûù":
        return True
    else:
        return False

# Test :
if __name__ == '__main__':
    ch ="gOàÉsùïÇ"               # lettres à tester
    for c in ch:
        print(c, ":", voyelle(c))

