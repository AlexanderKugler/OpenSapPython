# Week 6, Unit 3: Exercise (Python_1)

# Import the random library and have a look at the function gauss() which gives back a random float number. Which
# parameters are required? Write a function gaussian_distribution() that returns a list of 1000 random numbers with a
# mean of 100 and a standard deviation of 10. Invoke this function.

# For the resulting list calculate and print the mean and the standard deviation using the respective functions from
# the statistics library. Re-run the program and observe, if the values change.

# Below is the output of an example execution of the program. Note that the values of the standard derivation and the
# mean might be different in your case.

import random as r

def gaussian_distribution():
    numbers = [range(1000)]
    r.gauss(numbers, 10)
    return numbers


if __name__ == '__main__':
    print(r.gauss(10, 200))
