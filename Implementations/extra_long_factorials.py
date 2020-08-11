#this code in python is quite easy since python allows you to work on large numbers without any restrictions (except your available memory)
#however when it comes to writing the code in C/C++ you need to use BigIntegers to do the same.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    fact = 1
    while n>0:
        fact = fact*n
        n-=1
    print(fact)


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
