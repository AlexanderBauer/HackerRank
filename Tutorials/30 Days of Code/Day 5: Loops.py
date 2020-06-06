#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    x = 1
    while (x < 11):
        print(str(n) + ' x ' + str(x) + ' = ' + str(n*x))
        x += 1