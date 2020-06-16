def check_superset(a, b):
    return a.issuperset(b)

if __name__ == '__main__':
    a = set(map(int, input().split()))
    for _ in range(int(input())):
        output = check_superset(a, set(map(int, input().split())))
        if(output == False):
            break

    print(output)