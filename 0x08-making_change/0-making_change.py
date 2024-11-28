#!/usr/bin/python3
""" 0. Change comes from within """


def makeChange(coins, total):
    """ determine the fewest number of coins needed\
        to meet a given amount total """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
        if total == 0:
            return count
    return -1
