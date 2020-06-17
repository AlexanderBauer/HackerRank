from collections import namedtuple
n, student = int(input()), namedtuple('student',input())
print(sum( [int(student._make(input().split()).MARKS) for _ in range(n)]) / n)