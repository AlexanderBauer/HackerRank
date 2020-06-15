#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if(s[-2:] == 'PM' and s[:2] != '12'):
        output = str(int(s[:2]) + 12) + s[2:-2]
    elif(s[:2] == '12' and s[-2:] != 'PM'):
        output = '00' + s[2:-2]
    else:
        output = s[:-2]
    return output

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()