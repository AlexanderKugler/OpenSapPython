# Week 5, Unit 5: Exercise (Python_1)

# The stopping distance of a car can be calculated using the following rule of thumb:
#
# The stopping distance of the car is the sum of the reaction path and the brake distance The reaction path depends
# on the speed. It can be calculated by the following rule of thumb: The reaction path in meter is equal to the speed
# in km/h times 3/10. - Example: Speed 50km/h –> reaction path 15m The brake distance depends as well on the speed.
# Again there is a rule of thumb which is: brake distance in m is equal to the speed in km/h divided by 10,
# the result has to be taken by the power of 2 - Example: Speed 50km/h –> (50 / 10)**2 = 25m The stopping distance
# for a car with a speed of 50km/h is 15m + 25m = 40m

def reaction_path(speed):
    return speed * 3 / 10


def brake_distance(speed):
    return (speed / 10)**2


def stopping_distance(speed):
    return brake_distance(speed) + reaction_path(speed)


if __name__ == '__main__':
    speed_input = int(input("Speed"))
    print(reaction_path(speed_input))
    print(brake_distance(speed_input))
    print(stopping_distance(speed_input))