#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    result=[0,0]
    a1=0;
    b1=0;
    length=len(a)
    for i in range(length):
        if(a[i]<b[i]):
            b1=b1+1
        if(a[i]>b[i]):
            a1=a1+1
        if(a[i]==b[i]):
            a1=a1+0
            b1=b1+0
    result[0]=a1
    result[1]=b1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    
