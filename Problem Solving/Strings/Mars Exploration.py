#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    i, d = 0, 0
    for x in s:
        if(i % 3 == 1):
            if(x != 'O'):
                d += 1
        else:
            if(x != 'S'):
                d += 1
        i += 1
    return d

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()