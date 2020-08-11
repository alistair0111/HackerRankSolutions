#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the permutationEquation function below.
def permutationEquation(p):
    p1 = collections.deque(p)
    y=[]
    for i in range(len(p)):
        value = p1.index(i+1,0,len(p))
        value1 = p1.index(value+1,0,len(p))
        y.append(value1+1)
    return y
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
