#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # declare counter and result
    counter = 0
    result  = -99
    
    # loop through each hour glass
    for x in range(1,5):
        for y in range(1,5):
            # calculate sum
            counter = arr[x][y] + arr[x-1][y-1] + arr[x-1][y] + arr[x-1][y+1] + arr[x+1][y-1] + arr[x+1][y] + arr[x+1][y+1]
            # if larger then result, set new result
            if(counter > result):
                result = counter
            # reset counter
            counter = 0

    print(result)