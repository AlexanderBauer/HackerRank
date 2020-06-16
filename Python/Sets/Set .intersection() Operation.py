def intersect(a, b):
    return len(a.intersection(b))

if __name__ == '__main__':
    x, a, y, b = input(), set(input().split()), input(), set(input().split())
    print(intersect(a, b))