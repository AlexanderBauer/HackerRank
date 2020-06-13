import collections

money_earned        =   0
shoe_count          =   int(input())
shoe_collection     =   collections.Counter(map(int, input().split()))
customer_count      =   int(input())

for i in range(customer_count):
    size, price = map(int, input().split())
    if shoe_collection[size]: 
        money_earned            +=  price
        shoe_collection[size]   -=  1

print(money_earned)