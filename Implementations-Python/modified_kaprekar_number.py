#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    kap = []
    for i in range(p, q+1):
        if i == 1:
            kap.append(i)
        elif i>8:
            sq = str(i**2)
            if i == int(sq[0:len(sq)//2]) + int(sq[len(sq)//2:]): 
                kap.append(i) 
    if kap:
        print(' '.join(map(str,kap)))
    else:
        print('INVALID RANGE')
        
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
