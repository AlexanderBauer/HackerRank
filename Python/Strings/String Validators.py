if __name__ == '__main__':
    s    = input()
    line = [False, False, False, False, False]

    for i in s:
        if i.isalnum():
            line[0] = True
        if i.isalpha():
            line[1] = True
        if i.isdigit():
            line[2] = True
        if i.islower():
            line[3] = True
        if i.isupper():
            line[4] = True
       
    for x in line:
        print(x)