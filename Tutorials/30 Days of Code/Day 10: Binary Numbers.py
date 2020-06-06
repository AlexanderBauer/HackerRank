#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

# split consecutive numbers in arrays and count max len for each
ones        =   str(bin(n)[2:]).split('0')
zeros       =   str(bin(n)[2:]).split('1')
max_ones    =   len(max(ones, key=len))
max_zeros   =   len(max(zeros, key=len))
print(max(max_ones, max_zeros))