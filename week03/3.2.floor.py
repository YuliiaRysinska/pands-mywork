# Write a program that takes in a float and outputs an int rounded down
# !!!use math module math.floor()

import math
number_to_floor = float(input("Enter a float number:"))
floored_number = math.floor(number_to_floor)
print('{} floored is {}'.format(number_to_floor, floored_number))