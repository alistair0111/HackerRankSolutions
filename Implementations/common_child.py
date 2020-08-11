#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2,m,n):
 
    if m == 0 or n == 0: 
       return 0; 
    elif s1[m-1] == s2[n-1]: 
       return 1 + commonChild(s1, s2, m-1, n-1); 
    else: 
       return max(commonChild(s1, s2, m, n-1), commonChild(s1, s2, m-1, n));

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()
    m = len(s1)
    n = len(s2)

    result = commonChild(s1, s2,m,n)

    fptr.write(str(result) + '\n')

    fptr.close()
