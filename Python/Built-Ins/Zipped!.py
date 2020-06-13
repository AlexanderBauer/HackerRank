N, X    =   input().split()
marks   =   []
for _ in range(int(X)):
    marks.append(map(float, input().split()))
for i in zip(*marks): 
    print( round(sum(i) / len(i), 1) )