#!/bin/python3

import sys

# declare variables
n               =   int(input().strip())
a               =   list(map(int, input().strip().split(' ')))
i               =   0   # element counter - keeps track of current element
number_of_swaps =   0   # swap counter - keeps track of number of swaps done

while i < n:
    j = 0

    while(j < n -1):
        if(a[j] > a[j + 1]):
            # swap positions and increase swap count
            a[j], a[j + 1] = a[j + 1], a[j]
            number_of_swaps += 1
        j += 1

    if(number_of_swaps == 0):
        break
    
    # increase element counter
    i += 1

# print output
print("Array is sorted in " + str(number_of_swaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))