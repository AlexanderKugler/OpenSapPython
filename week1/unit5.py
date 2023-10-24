# Week 1, Unit 5: Exercise (Python_1)

# Write a Python program that asks the user to enter three integer numbers. The program should output the largest of
# the three numbers.

# Below is an example execution of the program:

first = int(input("Please enter the first number:"))
second = int(input("Please enter the second number"))
third = int(input("Please enter the third number"))

if first > second and first > third:
    print("The largest number is ", first)
elif second > first and second > third:
    print("The largest number is ", second)
elif third > first and third > second:
    print("The largest number is ", third)
