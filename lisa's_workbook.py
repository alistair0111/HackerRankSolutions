#!/bin/python3
import os
import math
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    special = 0
    pagecount=0
    for i in range(n):
        page=[]
        count=0
        for j in range(1,arr[i]+1):
            count+=1
            page.append(j)
            if count%k==0 or j==arr[i]:
                pagecount+=1
                if pagecount in page:
                    special+=1 
                page=[]
    return special 



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
