#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
     
    for i in range(d):
        a.append(a.pop(0))

    for i in a:
        print(i, end=" ")
