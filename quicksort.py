# QUICKSORT TEST
#   This program employs a quicksort algorithm on a list of integers from
#   an external txt file, and calculates the time taken,no. of comparisons and
#   no. of exchanges for the list to be sorted. The length of the list and the
#   time taken are appended in a separate file - quicksortResults.txt.

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
# Define functions for quicksort

# Execution function
def quicksort(A, comparisons=0, exchanges=0):
    A, comparisons, exchanges = quicksortHelper(A, 0, len(A)-1, comparisons, exchanges)
    return (A, comparisons, exchanges)

def quicksortHelper(A, low, high, comparisons, exchanges):
    if low<high:
        p, comparisons, exchanges = partition(A, low, high, comparisons, exchanges)
        A, comparisons, exchanges = quicksortHelper(A, low, p - 1, comparisons, exchanges)
        A, comparisons, exchanges = quicksortHelper(A, p+1, high, comparisons, exchanges)
        comparisons += 1
    else:
        comparisons += 1
    return (A, comparisons, exchanges)

# This function obtains the median value (pivot) from the lowest, highest, and
# middle indices
def getPivot(A, low, high, comparisons):
    mid = (low+high)//2
    pivot = high
    if A[low] < A[mid]:
        if A[high] < A[low]:
            pivot = low
            comparisons += 2
        if A[mid] < A[high]:
            pivot = mid
            comparisons += 3
    else:
        if A[high] < A[mid]:
            pivot = mid
            comparisons += 2
        if A[low] < A[high]:
            pivot = low
            comparisons += 3
    comparisons += 3 # +3 comparisons if pivot = high
    return (pivot, comparisons)

# This function sorts both sides of the pivot so that the left side is smaller
# and right is larger
def partition(A, low, high, comparisons, exchanges):
    pivotIndex, comparisons = getPivot(A, low, high, comparisons)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex] # swap pivot into left most
                                                  # position of list
    exchanges += 1
    border = low

    for i in range (low, high+1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
            comparisons += 1
            exchanges +=1
        else:
            comparisons += 1
    A[low], A[border] = A[border], A[low] # swap border and pivot. Now:
                                          # values left of pivot < pivot,
                                          # values right of pivot > pivot,
    exchanges += 1
    return (border, comparisons, exchanges) #returns the final pivot position

#-----------------------------------------------------------------------------
# Execute the function to sort list, A
A, comparisons, exchanges = quicksort(A)

# Calculate the time taken for this program to work
totalTime = time.time() - startTime

# Save this data in a separate txt file - quicksortResults.txt
with open("quicksortResults.txt", "a") as output:
    output.write(str(len(A)))
    output.write(", ")
    output.write(str(totalTime))
    output.write(", ")
    output.write(str(comparisons))
    output.write(",")
    output.write(str(exchanges))
    output.write("\n")
