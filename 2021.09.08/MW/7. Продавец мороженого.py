import sys

ice_creams = {}

for _ in range(int(input())):

    ice_cream = input().split('\t')
    name, price = ice_cream[0], int(ice_cream[1])
    ice_creams[name] = price

input()
prices = {1: 0}
count = 1
price_total = 0
for line in sys.stdin:
    line = line.strip()
    if line == '.':
        price_total += prices[count]
        break
    if line == '' and prices[count] != 0:
        price_total += prices[count]
        count += 1
        prices[count] = 0
    elif line == '':
        continue
    else:
        name, count_por = line.split('\t')
        prices[count] += ice_creams[name] * int(count_por)

for number, price in prices.items():
    if price != 0:
        print(f'{number}) {price}')
print(f'Итого: {price_total}')
