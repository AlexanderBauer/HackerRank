from collections import deque
d = deque()
for _ in range(int(input())):
    ops = input().split()    
    getattr(d, ops[0])(*[ops[1]] if len(ops) > 1 else [])
for x in d:
    print(x, end=' ')