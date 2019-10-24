#!/bin/python3

import math
import os
import random
import re
import sys
def matrixRotation(matrix, r,m,n):
    while(r>0):
        left=0
        top=0
        right=n-1
        bottom=m-1
        while left < right and top < bottom: 
            prev = matrix[top][left+1] 
            for i in range(top, bottom+1): 
                curr = matrix[i][left] 
                matrix[i][left] = prev 
                prev = curr 
            left+=1
            for i in range(left, right+1): 
                curr = matrix[bottom][i] 
                matrix[bottom][i] = prev 
                prev = curr 
            bottom-=1
            for i in range(bottom, top-1,-1): 
                curr = matrix[i][right] 
                matrix[i][right] = prev 
                prev = curr 
            right-=1 
            for i in range(right, left-1, -1): 
                curr = matrix[top][i] 
                matrix[top][i] = prev 
                prev = curr 
            top+=1
        r-=1

    printmat(matrix,m,n)

def printmat(mat,m,n):
    for i in range(m):
        for j in range(n):
            print(mat[i][j], end=" "),
        print()
        
        
        


#Alternate Method
#!/bin/python3
import math
import os
import random
import re
import sys
def matrixRotation(matrix, r,m,n):
    numrings=min(m,n)//2
    for i in range(numrings):
        numRotations = r%(2*(m + n - 4*i) - 4)
        for rotation in range(numRotations):
            for j in range(i,n-i-1):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][j+1]
                matrix[i][j+1]=temp
            for j in range(i,m-i-1):
                temp=matrix[j][n-i-1]
                matrix[j][n-i-1]=matrix[j+1][n-i-1]
                matrix[j+1][n-i-1]=temp
            for j in range(n-i-1,i,-1):
                temp=matrix[m-i-1][j]
                matrix[m-i-1][j]=matrix[m-i-1][j-1]
                matrix[m-i-1][j-1]=temp
            for j in range(m-i-1,i+1,-1):
                temp=matrix[j][i]
                matrix[j][i]=matrix[j-1][i]
                matrix[j-1][i]=temp

    
    
    printmat(matrix,m,n)

def printmat(mat,m,n):
    for i in range(m):
        for j in range(n):
            print(mat[i][j], end=" "),
        print()






if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r,m,n)
