#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    traverse = 0
    valleys = 0
    mountain = 0
    for idx in range(steps):
        if path[idx] == 'U':
            traverse+=-1
        else:
            traverse+=1
            
        if traverse == 0 and path[idx] == 'D':
                mountain+=1
        if traverse == 0 and path[idx] == 'U':
                valleys+=1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
