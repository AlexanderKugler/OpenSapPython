# Assignment Week 1 (Part 2 - Exercise)


if __name__ == '__main__':
    first = int(input("Please enter the first angle:"))
    second = int(input("Please enter the second angle:"))
    third = int(input("Please enter the third angle:"))
    summe = first + second + third

    if first < 0 or second < 0 or third < 0:
        print("Angles smaller than 0 are not valid.")
    elif summe > 180 or summe < 0:
        print("The entered values are not valid.")
    elif first == 90 or second == 90 or third == 90:
        print("The triangle is a right triangle.")
    elif first > 90 or second > 90 or third > 90:
        print("The triangle is a obtuse triangle.")
    elif first < 90 and second < 90 and third < 90:
        print("The triangle is a acute triangle.")
