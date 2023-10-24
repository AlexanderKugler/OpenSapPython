# Week 3, Unit 1: Exercise (Python_1)

# Write a program that asks the user for given name, surname and field of study for a student. Store this data in a
# tuple and print the tuple. Below is an example execution of the program.

# Please enter the given name of the student: Harry
# Please enter the surname of the student: Potter
# Please enter the field of study of the student: Defence Against the Dark Arts
# ('Harry', 'Potter', 'Defence Against the Dark Arts')

name = input("Please enter the given name of the student")
lastname = input("Please enter the surname of the student")
field = input("Please enter the field of study of the student:")

person = (name, lastname, field)

if __name__ == '__main__':
    print(person)
