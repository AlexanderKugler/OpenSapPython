# Week 4, Unit 3: Exercise (Python_1)

# The file numbers.txt contains random integer numbers. There is exactly one number per line. Read the file and
# output the three biggest numbers in the following form:

number_list = []

with open("numbers.txt", "r") as file:
    for line in file:
        line = line.strip()
        number_list.append(line)
        number_list.sort()

if __name__ == '__main__':
    print(number_list)
