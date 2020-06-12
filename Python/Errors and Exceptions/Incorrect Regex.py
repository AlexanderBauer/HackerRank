import re
for i in range(int(input())):
    result = True
    try:
        regx = re.compile(input())
    except re.error:
        result = False
    print(result)