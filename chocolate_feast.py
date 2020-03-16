#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    num_choc = 0
    num_choc = int(n/c)
    wrap = num_choc
    while wrap>=m:
        temp_wrap = int(wrap/m)
        num_choc+=temp_wrap
        wrap = num_wrap + (wrap%m)
    return num_choc
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
