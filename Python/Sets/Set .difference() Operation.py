def set_difference(a, b):
    return len(a.difference(b))

if __name__ == '__main__':
    x, a, y, b = input(), set(input().split()), input(), set(input().split())
    print(set_difference(a, b))