#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def checkSorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def almostSorted(arr):
    if len(arr) == 1 or checkSorted(arr):
        print("yes")
        return

    i = 0
    while i < len(arr) - 1 and arr[i] < arr[i+1]:
        i+=1
    first_left = i

    i = len(arr) - 1
    while i > 0 and arr[i-1] < arr[i]:
        i-=1
    first_right = i

    if (first_left == first_right):
        print("no")
        return

    l = first_left
    r = first_right
    swaps = 0
    while r-l > 0:
        if arr[l] > arr[r]: 
            arr[r], arr[l] = arr[l], arr[r]
            swaps += 1
        r-=1
        l+=1

    sorted_arr = checkSorted(arr)

    if sorted_arr:
        if swaps == 1:
            print("yes")
            print("swap {} {}".format(first_left+1,first_right+1))
        elif swaps == (first_right-first_left+1)//2:
            print("yes")
            print("reverse {} {}".format(first_left+1,first_right+1))
    else:
        print("no")



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
