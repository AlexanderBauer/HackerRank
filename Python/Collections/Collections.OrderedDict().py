from collections import OrderedDict
n       =   int(input())
Dict    =   OrderedDict()

for _ in range(n):
    product, space, price = input().rpartition(' ')
    Dict[product] = Dict.get(product, 0) + int(price)

for product, price in Dict.items():
    print(product, price)