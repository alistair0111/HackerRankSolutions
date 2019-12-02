#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0
    top = n - r_q
    bottom = r_q - 1
    right = n - c_q
    left = c_q - 1
    top_left = min(n - r_q, c_q - 1)
    top_right = n - max(c_q, r_q)
    bottom_left = min(r_q, c_q) - 1
    bottom_right = min(r_q - 1, n - c_q)
    
    for i in range(k):
        if obstacles[i][0] == r_q:
            if obstacles[i][1] > c_q:
                top = min(top, obstacles[i][1] - c_q - 1)
                continue
            else:
                bottom = min(bottom, c_q - obstacles[i][1] - 1)
                continue
    
        elif obstacles[i][1] == c_q:
            if obstacles[i][0] > r_q:
                right = min(right, obstacles[i][0] - r_q - 1)
                continue
            else:
                left = min(left, r_q - obstacles[i][0] - 1)
                continue
    # diagonals
        elif abs(obstacles[i][1] - c_q) == abs(obstacles[i][0] - r_q):
        # top right
            if obstacles[i][1] > c_q and obstacles[i][0] > r_q:
                top_right = min(top_right, obstacles[i][1] - c_q - 1)
                continue
        # bottom right
            elif obstacles[i][1] > c_q and obstacles[i][0] < c_q:
                bottom_right = min(bottom_right, obstacles[i][1] - c_q - 1)
                continue
        # top left
            elif obstacles[i][1] < c_q and obstacles[i][0] > r_q:
                top_left = min(top_left, c_q - obstacles[i][1] - 1)
                continue
        # bottom left
            elif obstacles[i][1] < c_q and obstacles[i][0] < r_q:
                bottom_left = min(bottom_left, c_q - obstacles[i][1] - 1)
                continue

    count = top + bottom + right + left + top_left + top_right + bottom_right +bottom_left
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
