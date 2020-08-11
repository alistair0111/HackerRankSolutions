#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    minimum = len(a)
    d = dict()
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = i
        else:
            minimum = min(minimum,i-d[a[i]])
    if minimum == n:
        return -1
    else:
        return minimum
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
