# Short version: An inversion occurs when the a given value in an array precedes another value in the array.

# For instance, in an array of (random picks here): 3 1 4 5 6 2

# 1 is preceded by higher value 3, so that's 1 inversion. 3, 4, 5, and 6 each precede the lower value 2, so that's 1 inversion each.

# For this problem, the array can be solved with the given formula if the total number of inversions is even/divisible by 2.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.

def larrysArray(A):
    sum1=0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                sum1+=1
    if(sum1%2):
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
