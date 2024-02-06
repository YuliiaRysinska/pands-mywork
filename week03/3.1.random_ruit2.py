# This program prints out a random fruit (tuple)
import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')

# Random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit: {}".format(fruit))