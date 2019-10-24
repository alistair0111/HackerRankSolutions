                                                                                                                                                                                                                                                                                                                                                                                                                                                                       #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    arrived_late=0
    arrived_ontime=0
    for i in range(len(a)):
        if(a[i]<=0):
            arrived_ontime+=1
        elif(a[i]>0):
            arrived_late+=1
    if(arrived_ontime>=k):
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
