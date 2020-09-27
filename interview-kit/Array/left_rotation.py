#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    length = len(a)
    if d>length:    
        d = d%length
    temp_arr = []
       #cant pass all test case
    # for idx in range(length-mod):
    #     temp_arr.append(a[idx])
    # for i in range(len(a) - 1, -1, -1):
    #     if i-mod < 0:
    #         if i<= length-mod-1:
    #             a[i-mod+length] = temp_arr[i]
    #         else:
    #             a[i-mod+length] = a[i]
    #     else:
    #         a[i-mod] = a[i]
       #passed all test case but need aditional space
    for i in range(length):
        if i+d < length:
            temp_arr.append(a[i+d]) 
        else:
            temp_arr.append(a[(i+d)-length]) 
       #best solution
    #a[((n- (k%n))+i)%n] = a[i]
    return temp_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
