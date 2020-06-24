import numpy as np

N, M = map(int, input().split())
data = list()
for _ in range(N):
    data.append(input().split())

data = np.array(data, int)
print(np.max(np.min(data, axis=1)))