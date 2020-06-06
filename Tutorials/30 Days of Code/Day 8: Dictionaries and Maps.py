# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

# build book
book    =   {}
x       =   0

while x < n:
    # build book
    a,b     =   input().split()
    book[a] =   b
    x       +=  1

# search book
try:
    while True:
        name = input()
        if name in book:
            print(name + '=' +book[name])
        else:
            print('Not found')  
except EOFError:
    pass