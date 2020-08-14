#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    i=0
    commonlength = 0
    while i<min(len(s),len(t)):
        if(s[i]==t[i]):
            commonlength+=1
        else:
            break
        i+=1
    if((len(s)+len(t))<=k):
        return "Yes"
    if((k-len(s)-len(t)+2*commonlength)%2==0 and (k-len(s)-len(t)+2*commonlength)>=0):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
