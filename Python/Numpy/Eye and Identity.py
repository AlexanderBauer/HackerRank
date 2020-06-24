import numpy

N, M = input().split()
numpy.set_printoptions(sign=' ')
print(numpy.eye(int(N), int(M)))