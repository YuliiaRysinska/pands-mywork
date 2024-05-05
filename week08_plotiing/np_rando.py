#program that makes a list, called salaries, that has (say 10) random numbers (20000 – 80000)
import numpy as np
import matplotlib.pyplot as plt

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug.

salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)

salariesPlus = salaries + 5000 # this will add 5000 to each value
print(salariesPlus)

salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05
print(salariesMult)
# This is a float array, here I convert it to an int array (it does a floor)
newSalaries = salariesMult.astype(int)
print(newSalaries)

#Write a program that plots a histogram
plt.hist(salaries)
plt.show()