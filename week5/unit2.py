# Week 5, Unit 2: Exercise (Python_1)

# Implement a function named get_student_data(). The function should do the following:

# Using input() it asks for name, first name and a student-id.
# The values are packed into a tuple.
# This tuple is returned from the function
# The function get_student_data() is then called in the program, the return value is assigned to a variable.
# Finally, output the variable using print().

def get_student_data():
    name = input("What is your name?")
    first_name = input("What is your first name?")
    student_id = input("What is your Student-ID?")

    student_info = (name, first_name, student_id)

    return student_info


if __name__ == '__main__':
    print(get_student_data())
