#1. Write a function that reads in a number from a file that already exists(count.txt). test the program by 
# calling the function and outputting the number.

FILENAME = "count.txt"
def readNumber():
 with open(FILENAME) as f:
    number = int(f.read())
    return number
# test it
num = readNumber()
print (num)

#2. Write a function that takes in a number and overwrites a file with that
#number (count.txt). test it and check that the file has been changed
def writeNumber(number):
 with open(FILENAME, "wt") as f:
 # write takes a string so we need to convert
    f.write(str(number))
# test it
writeNumber(3)

#3. Write a program that, uses these two functions, to count how many times
#the program has been run. Test it, check to see that the number goes up each time.
FILENAME = "count.txt"
def readNumber():
 with open(FILENAME) as f:
    number = int(f.read())
    return number
def writeNumber(number):
 with open(FILENAME, "wt") as f:
 # write takes a string so we need to convert
    f.write(str(number))
# main
num = readNumber()
num += 1
print (f"we have run this program {num} times")
writeNumber(num)

#Write some code to check if the file exists. To do this we will need to import
#os.path and use the isfile() function. You would need to look this up
import os.path
FILENAME = "count.txt"
if not os.path.isfile(FILENAME):
 print ("File does not exist")
 #initialise file here
 writeNumber(0)
 
 # Use a try catch loop on the read (I think the best way).
def readNumber():
 try:
    with open(FILENAME) as f:
        number = int(f.read())
    return number
 except IOError:
 # this file will be created when we write back.
 # no file assumes first time running
 # ie 0 previous runs
    return 0

# Write a function that will store a simple Dict to a file as JSON
import json
FILENAME="testdict.json"
sample= dict(name='fred', age=31, grades=[1,34,55])

def writeDict(obj):
 with open(FILENAME, 'wt') as f:
    json.dump(obj,f)
#test the function
writeDict(sample)

# Write a function that will read in a dict object from file
import json
FILENAME ="testdict.json"

def readDict():
 # this will throw an error if the file does not exist
 # it should readly just return an empty dict
 # we can do this later
 with open(FILENAME) as f:
    return json.load(f)
# test the function
somedict = readDict()
print(somedict)