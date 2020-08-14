#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the timeInWords function below.
def timeInWords(h, m):
    nums = [ "zero", "one", "two", "three", "four", 
                        "five", "six", "seven", "eight", "nine", 
                        "ten", "eleven", "twelve", "thirteen", 
                        "fourteen", "fifteen", "sixteen", "seventeen", 
                        "eighteen", "nineteen", "twenty", "twenty one", 
                        "twenty two", "twenty three", "twenty four", 
                        "twenty five", "twenty six", "twenty seven", 
                        "twenty eight", "twenty nine"]
    if (m == 0):
        return nums[h]+" o' clock" 
  
    elif (m == 1):
        return "one minute past "+nums[h] 
  
    elif (m == 59):
        return "one minute to "+nums[(h % 12) + 1] 
  
    elif (m == 15): 
        return "quarter past "+ nums[h] 
  
    elif (m == 30):
        return "half past "+nums[h] 
  
    elif (m == 45):
        return "quarter to " + nums[(h % 12) + 1] 
  
    elif (m <= 30):
        return nums[m]+" minutes past "+nums[h]
  
    elif (m > 30):
        return nums[60-m]+" minutes to "+nums[(h % 12) + 1]
    # d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 :'five',
    #       6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
    #       11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
    #       15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
    #       19 : 'nineteen', 20 : 'twenty',
    #       30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
    #       70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    # if m==15:
    #     time = 'quarter past '+d[h]
    #     return time
    # elif m==0:
    #     time = d[h]+' o\' clock'
    #     return time
    # elif m==45:
    #     time = 'quarter to '+d[h+1]
    #     return time
    # elif m==30:
    #     time = 'half past '+d[h+1]
    # elif 0<m<30 and m!=15:
    #     if m == 1:
    #         time = d[m]+' minute past '+d[h]
    #         return time
    #     elif m<20:
    #         time = d[m]+' minutes past '+d[h]
    #         return time
    #     elif m>=20 and m%10==0:
    #         time = d[m]+' minutes past '+d[h]
    #         return time
    #     elif m>=20 and m%10!=0:
    #         time = d[m]+' '+d[m%10]+' minutes past '+d[h]
    #         return time
    # elif 30<m<=59 and m!=15:
    #     if m%10==0:
    #         time = d[60-m]+' minutes to '+d[h+1]
    #         return time
    #     elif m%10!=0:
    #         temp = 60-m
    #         if temp ==1:
    #             time = d[temp]+ ' minute to '+d[h+1]
    #             return time
    #         elif temp<=20:
    #             time = d[temp]+' minutes to '+d[h+1]
    #             return time
    #         elif temp>20:
    #             time = d[temp]+' '+d[temp%10]+' minutes to '+d[h+1]
    #             return time
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
