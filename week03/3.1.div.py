# Write a program (div.py) that reads in two numbers
x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

# And divides (//) the first one by the second
answer = int(x//y) 

# And gives the remainder (%)
remainder = x % y 

# Print out
print("{} divided by {} is {} with remainder {}".format( x, y, answer, remainder))

