# Simple Calculator

def multiply(a, b):
    return a + b


def divde(a, b):
    return a / b


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def calc(a, b):
    if readline == "+":
        print("Ergebnis: ", plus(a, b))
    elif readline == "-":
        print("Ergebnis: ", minus(a, b))
    elif readline == "*":
        print("Ergebnis: ", multiply(a, b))
    elif readline == "/":
        print("Ergebnis:", divde(a, b))


if __name__ == '__main__':
    # Calc eingabe
    readline = input("Was willst du machen ")
    print("Aktion: ", readline)

    number1 = int(input("Gib die erste Zahl ein: "))
    print("Nummer 1: ", number1)

    number2 = int(input("Gib die zweite Zahl ein: "))
    print("Nummer 2: ", number2)
