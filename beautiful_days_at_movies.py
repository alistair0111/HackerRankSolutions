#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reverse(Number):
    Reverse=0
    while(Number > 0):
        Reminder = Number%10
        Reverse = (Reverse *10) + Reminder
        Number = Number //10
    return Reverse
def beautifulDays(i, j, k):
    count=0
    for i in range(i,j):
        rev=reverse(i)
        if(abs(i-rev)%k==0):
            count+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
