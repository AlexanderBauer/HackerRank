#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s): 
    valleys =   0 
    ups     =   0 
    downs   =   0 
    for step in list(s): 
        if step == 'U': 
            ups += 1 
            if(ups == downs): 
                valleys += 1 
        else: 
            downs += 1 
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()