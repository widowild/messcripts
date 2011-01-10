#! /usr/bin/env python
# -*- coding:Utf8 -*-

def majuscule(car):
    "renvoie <vrai> si le caractère 'car' est une majuscule"
    car = car.decode("Utf8")       # conversion string -> unicode
    if car in u"ABCDEFGHIJKLMNOPQRSTUVWXYZÀÉÈÊËÇÎÏÂÙÔ":
        return 1
    else:
        return 0

# Test :
if __name__ == '__main__':
    print majuscule('d'), majuscule('É')
