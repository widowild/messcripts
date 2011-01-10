#! /usr/bin/env python
# -*- coding:Utf8 -*-

def estUneMaj(car):
    "renvoie <vrai> si le caractère 'car' est une majuscule"
    if car in "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÉÈÊËÇÎÏÙÜÛÔÖ":
        return True
    else:
        return False

# Test :
if __name__ == '__main__':
    caracteres ="eÀçMöSÖÛmÇéùT"
    print("Caractères à tester :", caracteres)
    for car in caracteres:
        print(car, estUneMaj(car))

