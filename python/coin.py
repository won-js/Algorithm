n, money = map(int,input().split(" "))

coins = []
count = 0

for _ in range(n):
    coins.append(int(input()))

while money != 0:
    for coin in coins[::-1]:
        count += money//coin
        money = money%coin

print(count)