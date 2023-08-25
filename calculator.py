# Simple Calculator

def multiply(a, b):
    return a + b


def divde(a, b):
    return a / b


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def calc(number1, number2):
    if readline == "+":
        print("Ergebnis: ", plus(number1, number2))
    elif readline == "-":
        print("Ergebnis: ", minus(number1, number2))
    elif readline == "*":
        print("Ergebnis: ", multiply(number1, number2))
    elif readline == "/":
        print("Ergebnis:", divde(number1, number2))


if __name__ == '__main__':
    # Calc eingabe
    readline = input("Was willst du machen ")
    print("Aktion: ", readline)

    number1 = int(input("Gib die erste Zahl ein: "))
    print("Nummer 1: ", number1)

    number2 = int(input("Gib die zweite Zahl ein: "))
    print("Nummer 2: ", number2)
