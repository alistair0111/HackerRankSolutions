#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    lindex=sum=0     
    uindex=1         
    listcount=[]
    
    while lindex!=len(topic)-2:
        if uindex > len(topic)-1:
            lindex+=1
            uindex=lindex+1
        res=bin(int(topic[lindex],2) | int(topic[uindex],2)) #counts total topics known using bitwise operation
        temp_count=res.count(str(1))
        uindex+=1
        if temp_count >= sum:
            sum = temp_count
            listcount.append(sum)
    return (sum,listcount.count(sum))

        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
