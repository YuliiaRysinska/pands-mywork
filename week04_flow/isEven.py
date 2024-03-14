#program asks the user to enter in a number, and it will tell the user if the number is even or odd.
number = int(input("Enter an integer:"))
if (number % 2) == 0:
    print (number, "is an even number")
else:
    print(number, "is an odd number")
