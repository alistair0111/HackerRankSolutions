#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    Seqs = [ [] for _ in range( n ) ]
    for _ in range( Q ):
        t, x, y = map( int, input().split() )
        if t == 1:
            Seqs[ ( x ^ lastans ) % N ].append( y )
        elif t == 2:
            arr = Seqs[ ( x ^ lastans ) % N ]
            val = arr[ y % len(arr) ]
            print( val )
            lastans = val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
