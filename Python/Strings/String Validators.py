if __name__ == '__main__':
    s       =   input()
    line1   =   line2 = line3 = line4 = line5 = False

    for i in s:
        if i.isalnum():
            line1 = True
        if i.isalpha():
            line2 = True
        if i.isdigit():
            line3 = True
        if i.islower():
            line4 = True
        if i.isupper():
            line5 = True
            
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)