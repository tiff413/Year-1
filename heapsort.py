# HEAPSORT TEST
#   This program employs a heapsort algorithm on a list of integers from
#   an external txt file, and calculates the time taken, no. of comparisons and
#   no. of exchanges for the list to be sorted. These results and the length of
#   the list are appended onto a separate file.

import time

#-----------------------------------------------------------------------------
# Extract list from the external .txt file and call this list A
A = []

with open("100k.txt", "r") as readFile:
  for line in readFile:
    A.append(int(line.strip()))

#-----------------------------------------------------------------------------
# Take the start time
startTime = time.time()
#-----------------------------------------------------------------------------
# Define functions

# Execution function
def heapsort(A, comparisons, exchanges):
    # Convert list to heap
    length = len(A)-1
    leastParent = int(length/2)
    for i in range(leastParent, -1, -1):
        A, comparisons, exchanges = moveDown(A, i, length, comparisons, exchanges)

    # Flatten heap into sorted array
    for i in range(length, 0, -1):
        if A[0] > A[i]:
            A, exchanges = swap(A, 0, i, exchanges)
            A, comparisons, exchanges = moveDown(A, 0, i-1, comparisons, exchanges)
            comparisons +=1
    return (A, comparisons, exchanges)

def moveDown(A, first, last, comparisons, exchanges):
    largest = 2*first + 1
    while largest <= last:
        comparisons += 1
        # right child exists and is larger than left child
        if (largest < last) and (A[largest] < A[largest+1]):
            largest += 1
            comparisons += 2
        # right child is larger than parent
        if A[largest] > A[first]:
            A, exchanges = swap(A, largest, first, exchanges)
            first = largest;
            largest = 2*first + 1
            comparisons += 1
        else:
            return (A, comparisons, exchanges) # force exit
    return (A, comparisons, exchanges)

def swap(B, x, y, exchanges):
    temp = B[x]
    B[x] = B[y]
    B[y] = temp
    exchanges += 1
    return (B, exchanges)

#-----------------------------------------------------------------------------
# Execute function to sort list, A
A, comparisons, exchanges = heapsort(A, comparisons=0, exchanges=0)

# Calculate the time taken for this program to work
totalTime = time.time() - startTime

# Save this data in a separate txt file - heapsortResults.txt
with open("heapsortResults.txt", "a") as output:
    output.write(str(len(A)))
    output.write(", ")
    output.write(str(totalTime))
    output.write(", ")
    output.write(str(comparisons))
    output.write(",")
    output.write(str(exchanges))
    output.write("\n")
