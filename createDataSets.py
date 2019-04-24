# This program creates a list of random integers that are ready to be tested by
# the heapsort and quicksort algorithms.

import random as rd

#------------------------------------------------------------------------------
# Create a list of random integers and store it in a separate file
B = []
listSize = 10000

for i in range(0,listSize):
    x =  rd.randint(1,10000)
    B.append(x)

with open("100k.txt", "w") as writeFile:
    for values in B:
        writeFile.write(str(values) + "\n")

print("All done")
