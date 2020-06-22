import re

S, k    =   input(), input()
counter =   0
match   =   0

while counter < len(S):
    m = re.search(r''+k, S[counter:counter+len(k)])
    if(m):
        match   =   1
        print((counter + m.start(), counter + m.end() - 1))
    counter += 1

if(match == 0):
    print((-1, -1))