#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    count=0
    sumval=0
    tempsum=0
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            tempsum=keyboards[i]+drives[j]
            if(tempsum>sumval and tempsum<=b):
                sumval=tempsum
                count+=1
    if(count>0):
        return sumval
    else:
        return -1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
