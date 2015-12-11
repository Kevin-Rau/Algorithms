# Name: Kevin Rau
# Email: Kevin.Rau@colorado.edu
# SUID: 101289616
#

import sys
import random
import time

# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)
    return retList

#------ Merge Sort --------------
def mergeSort(lst):
    if len(lst) <= 1:
        return lst
 
    mid = len(lst) / 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
 
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:   
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
 
    if len(left) > 0:
        result.extend(mergeSort(left))
    else:
        result.extend(mergeSort(right))
 
    return result

#def partition(lst, first, last):
#    pivot = lst[first]
#    left = first + 1
#    right = last
#    complete = False
#    while(not complete):
#        while(left<=right and lst[left] <= pivot):
#            left = left + 1
#        while(lst[right] >= pivot and right >= left):
#            right = right -1
#        if (rigt<left):
#           complete = True
#        else:
#            tempArray = lst[left]
#            lst[left] = lst[right]
#            lst[right] = tempArray 
#    tempArray = lst[first]
#    lst[first] = lst[right]
#    lst[right] = tempArray  
#    return right


#------ Quick Sort --------------
def quickSort(lst):
    if len(lst)<2: return lst
    pivot_element = random.choice(lst)
    small = [i for i in lst if i< pivot_element]
    medium = [i for i in lst if i==pivot_element]
    large = [i for i in lst if i> pivot_element]
    return quickSort(small) + medium + quickSort(large)

#    if (first < last):
#        pivotElement = partition(lst, first, last)
#        quickSort(lst, first, pivotElement-1)
#        quickSort(lst, pivotElement+1, last)
#    return lst
# ------ Timing Utility Functions ---------

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)


def timeToRun():
    time1 = measureRunningTimeComplexity(quickSort, generateRandomList)
    time2 = measureRunningTimeComplexity(insertionSort, generateRandomList)
    time3 = measureRunningTimeComplexity(mergeSort, generateRandomList)
    return time1, time2, time3
    print("time for insertion: ", time1)
    print("time for merge: ", time2)
    print("time for quick: ", time3)
