def mutations(base_set, op, new_set):
    return getattr(base_set, op)(new_set)

if __name__ == '__main__':
    n, a    =   input(), set(map(int, input().split()))
    for _ in range(int(input())):
        op  =   input().split()
        mutations(a, op[0], set(map(int, input().split())))
    print(sum(a))