# !!!rounds a number to the nearest even number: eg 4.5 = 4 but 5.5 = to 6)
# Write a program  what take in a float and output an int (rounded up or down)

number_to_round = float(input("Enter a float number:"))
rounded_number = round(number_to_round)
print ( '{} rounded is {}'.format(number_to_round,rounded_number))