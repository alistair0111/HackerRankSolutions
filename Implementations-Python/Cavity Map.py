#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    carry = 0
    loaf = 0
    for i in B:
        if (carry+i)%2:
            carry = 1
            loaf += 2  
        else:
            carry = 0
    return "NO" if carry else loaf


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
