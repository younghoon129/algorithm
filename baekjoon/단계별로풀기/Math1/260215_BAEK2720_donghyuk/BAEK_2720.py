t = int(input())
coins = [25, 10, 5, 1]
for _ in range(t):
    money = int(input())
    result = []
    for coin in coins:
        result.append(money // coin)
        money %= coin
    print(*result)