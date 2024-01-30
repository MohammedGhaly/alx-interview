#!/usr/bin/python3
'''module containing makeChange function'''


def makeChange(coins, total):
    '''
    gets the fewest number of coins to meet a given amount total
    '''
    if total <= 0:
        return 0
    n = len(coins)
    sorted_coins = sorted(coins, reverse=True)
    coin_index = 0
    coins_counter = 0
    while total > 0:
        if coin_index >= n:
            return -1
        if total - sorted_coins[coin_index] >= 0:
            total -= sorted_coins[coin_index]
            coins_counter += 1
        else:
            coin_index += 1
    return coins_counter
