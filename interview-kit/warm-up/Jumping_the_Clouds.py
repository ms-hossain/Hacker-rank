#!/bin/python3

import math
import os
import random
import re
import sys
#commented solution generates wrong solution some test case.
# Complete the jumpingOnClouds function below.
# def jumpingOnClouds(c):
#     result = 0
#     idx = 0
#     length = len(c)
#     if length%2==0 and c[length-1] == 0:
#             result+=1
#     while(idx<length-2):
#         if c[idx+2]==0:
#             result+=1
#             idx+=2
#         else:
#             idx+=1
#             result+=1
        
#     return result

def jumpingOnClouds(c):
    if len(c) == 1 : return 0
    if len(c) == 2: return 0 if c[1]==1 else 1
    if c[2]==1: 
        return 1 + jumpingOnClouds(c[1:])
    if c[2]==0:
        return 1 + jumpingOnClouds(c[2:])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
