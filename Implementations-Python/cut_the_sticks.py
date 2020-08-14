#!/bin/python3

import math
import os
import random
import re
import sys 

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result=[]
    resultcount=0
    while(len(arr)!=0):
        n=min(arr)
        count=arr.count(n)
        result.append(len(arr))
        for i in range(count):
            arr.remove(n)
        for i in range(len(arr)):
            arr[i]=arr[i]-n
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
