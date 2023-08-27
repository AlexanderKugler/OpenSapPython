#Password Generator
import string
from random import random

if __name__ == '__main__':

    passwordLength = int(input("Wie lang soll das Passwort sein? "))
    number = input("Soll das Passwort Zahlen enthalten? (y/n) ")
    special = input("Soll das Passwort Sonderzeichen enthalten? (y/n) ")

    if number == "y" and special == "y":
        for i in range(passwordLength):
            print(string.ascii_letters[int(random() * len(string.digits))], end="")
    elif number == "y" and special == "n":
        for i in range(passwordLength):
            print(string.ascii_letters[int(random() * len(string.digits))], end="")
    elif number == "n" and special == "y":
        for i in range(passwordLength):
            print(string.ascii_letters[int(random() * len(string.digits))], end="")
    elif number == "n" and special == "n":
        for i in range(passwordLength):
            print(string.ascii_letters[int(random() * len(string.digits))], end="")
    else:
        print("Falsche Eingabe")