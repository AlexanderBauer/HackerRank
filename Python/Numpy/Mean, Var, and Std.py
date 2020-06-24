import numpy as np

N, M = map(int, input().split())
data = list()
for _ in range(N):
    data.append(input().split())

data = np.array(data, int)
np.set_printoptions(legacy='1.13')
print(np.mean(data, axis= 1))
print(np.var(data,  axis= 0))
print(np.std(data,  axis = None))