_, a, _, b = input(), set(input().split()), input(), set(input().split())
x = a.difference(b)
y = b.difference(a)
z = x.union(y)
for i in sorted(z, key=float):
    print(i)