# Enter your code here. Read input from STDIN. Print output to STDOUT
# reading n and looping for n times
for i in range(0, int(input())):
    # declaring variables
    even = odd = ''
    char = 0
    # looping through chars and checking for indexes
    for x in input():
        if(char % 2 == 0):
            even    +=      x
        else:
            odd     +=      x
        char        +=      1
    print(even + ' ' + odd)