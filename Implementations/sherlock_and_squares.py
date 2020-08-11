#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the squares function below.
# mathematical solution
def squares(a, b):
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a-1))
    return count

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
