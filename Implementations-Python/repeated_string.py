#!/bin/python3
import math
import os
import random
import re
import sys
import collections
# Complete the repeatedString function below.
def repeatedString(s, n):

    if(n!=0):
        mul = n%len(s)
        multiplier = n//len(s)
    count = 0
    for i in range(len(s)):
        count = s.count("a")
        if(n!=0):
            count=count*multiplier
        if(mul!=0):
            for i in range(mul):
                if s[i]=="a":
                    count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
