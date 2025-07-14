'''
Coins: [1, 2, 5, 10, 20, 50, 100, 500, 2000]
Amount: 93
Coins used: [50, 20, 20, 2, 1]
'''
def foo(coins, amount):
    coins.sort(reverse = True)
    coinsUsed = []

    for coin in coins:
        while amount >= coin:
            coinsUsed.append(coin)
            amount -= coin

    return coinsUsed

print(foo([1, 2, 5, 10, 20, 50, 100, 500, 2000], 93))
