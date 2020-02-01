#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    # listindex = list(combinations(range(0,len(arr)),3))
    # count=0
    # for i in range(0,len(listindex)):
    #     if arr[listindex[i][0]] and arr[listindex[i][2]]-arr[listindex[i][1]]==d:
    #         count+=1
    # return count
    count = 0
    for i in range(0,len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            count+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
