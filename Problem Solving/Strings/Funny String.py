#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    a, b = [], []
    for i in range(1, len(s)):
        a.append(abs(ord(s[i]) - ord(s[i-1])))
        b.append(abs(ord(s[len(s) - i]) - ord(s[len(s) - i - 1])))
    if(a == b):
        return 'Funny'
    else:
        return 'Not Funny'
    
    # alternative solution
    #for i in range(1, len(s)):
    #    if(abs(ord(s[i])-ord(s[i-1])) != abs(ord(s[len(s) - i]) - ord(s[len(s) - i - 1]))):
    #        return 'Not Funny'    
    #return 'Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()