import math
# T = number of test cases
T = int(input())

for i in range(0, T):
    n = int(input())

    if(n > 1): 
        result = "Prime"
    else:
        result = "Not prime"

    # calculate square root and check dividend for range
    sq = int(math.sqrt(n))
    for dividend in range(2, sq + 1):
        if(n % dividend == 0):
            result = "Not prime"
            break

    # print result
    print(result)