n, m    =   input().split()
arr     =   input().split()
a       =   set(input().split())
b       =   set(input().split())
score   =   0

for x in arr:
    if x in a:
        score += 1
    if x in b:
        score -= 1

print(score)