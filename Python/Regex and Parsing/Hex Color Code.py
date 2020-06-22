import re

for _ in range(int(input())):
    line    =   input()
    matches =   re.findall(r'.(#[0-9A-Fa-f]{3,6})', line)
    for match in matches:
            print(match)