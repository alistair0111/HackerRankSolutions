#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    p1=[[4,9,2],[3,5,7],[8,1,6]]
    p2=[[8,3,4],[1,5,9],[6,7,2]]
    p3=[[6,1,8],[7,5,3],[2,9,4]]
    p4=[[2,7,6],[9,5,1],[4,3,8]]
    s1,s2,s3,s4,s5,s6,s7,s8=0,0,0,0,0,0,0,0
    for i in range(3):
        for j in range(3):
            s1+=abs(s[i][j]-p1[i][j])
            s2+=abs(s[i][j]-p1[i][2-j])
            s3+=abs(s[i][j]-p2[i][j])
            s4+=abs(s[i][j]-p2[i][2-j])
            s5+=abs(s[i][j]-p3[i][j])
            s6+=abs(s[i][j]-p3[i][2-j])
            s7+=abs(s[i][j]-p4[i][j])
            s8+=abs(s[i][j]-p4[i][2-j])
        
    ans=min(min(min(s1,s2),min(s3,s4)),min(min(s5,s6),min(s7,s8)))
    return ans
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
