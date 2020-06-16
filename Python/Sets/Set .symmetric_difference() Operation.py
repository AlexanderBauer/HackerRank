def symmetric_diff(a, b):
    return len(a.symmetric_difference(b))

if __name__ == '__main__':
    x, a, y, b = input(), set(input().split()), input(), set(input().split())
    print(symmetric_diff(a, b))