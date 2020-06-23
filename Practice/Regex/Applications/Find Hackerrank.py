import re

def scoring(s):
    if re.search(   r'^hackerrank$',    s):
        return 0
    elif re.search( r'^hackerrank',     s):
        return 1
    elif re.search( r'hackerrank$',     s):
        return 2
    else:
        return -1

for _ in range(int(input())):
    print(scoring(input()))