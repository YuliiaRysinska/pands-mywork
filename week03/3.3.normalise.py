# Write a prog that reads in a string and strips any leading and trailing spaces and program should also convert the string to lower case.

raw = input("Please enter a string:")
normalised_string = raw.strip().lower()

# program should also output the length of the input and output strings
len_of_raw = len(raw)
len_of_norm = len(normalised_string)

print(f"That String normalised is:{normalised_string}")

print(f"we reduced the input string from {len_of_raw} to {len_of_norm } characters")
