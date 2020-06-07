#!/bin/python3

import math
import os
import random
import re
import sys

n               =   int(input())
first_names     =   []
for i in range(0, n):
    regex_match = re.findall(r"^[a-z]*[ ][a-z.]*[@]gmail[.]com$", input())
    if(regex_match):
        # if list is not empty, split match by space to get first name
        splitted = regex_match[0].split()
        first_names.append(splitted[0])

# sort and print names
first_names.sort()
for x in first_names:
    print(x)