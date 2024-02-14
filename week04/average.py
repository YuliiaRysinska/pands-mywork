# Prog that keeps reading numbers until the userenters 0. (the program should append each of them into a list)
# the program should then print out each of the numbers entered and the average of them.
numbers = []
# first number then we check if it is 0 in the while loop
number = int(input("Enter number (0 to quit): "))
while number != 0:
    numbers.append(number)
    # read the next number and check if 0
    number = int(input("Enter another (0 to quit): "))
for value in numbers:
    print(value)
# I want average to be a float
average = float(sum(numbers)) / len(numbers)
print(f"The average is {average}")
