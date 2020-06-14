from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = list(product(a, b))
for i in p:
    print(i, end=' ')