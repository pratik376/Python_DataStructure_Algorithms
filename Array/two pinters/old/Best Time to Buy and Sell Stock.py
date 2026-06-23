num=[7,6,4,3,1]

min_price=num[0]

profit=0

for price in range(1,len(num)):

    if num[price] > min_price:
        profit=num[price]-min_price
    else:
        min_price=num[price]

print(profit)
