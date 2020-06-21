import re

for _ in range(int(input())):
    try:
        assert re.match(r'^[+-\.]?(\d+)?[\.]\d+$', input())
    except:
        print('False')
    else:
        print('True')