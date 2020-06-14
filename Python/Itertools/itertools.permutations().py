from itertools import permutations
S, k    =   input().split()
p       =   list(permutations(sorted(S), int(k)))
for x in p:
    print(''.join(x))