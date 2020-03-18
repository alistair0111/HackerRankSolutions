#!/bin/python3

import math
import os
import random
import re
import sys
# not my solution found this on stackoverflow.
# tried solving but couldn't get a more optimized solution
# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    best = ''
    for i in range(len(w)):
        idx = -i-1
        c = w[idx]
        if c >= best:
            best = c
        else:
            l = sorted(w[idx:])
            for j, ch in enumerate(l):
                if ch > c:
                    return w[:idx] + ch + ''.join(l[:j] + l[j+1:])
    return 'no answer'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
