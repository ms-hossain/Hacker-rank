#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    num_pairs = 0
    cnt = [0 for zero in range(100000)]
    for idx in range(n):
        cnt[ar[idx]]  = 1 + cnt[ar[idx]]
    for idx in range(len(cnt)):
        num_pairs += int(cnt[idx]/2)
    return num_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
