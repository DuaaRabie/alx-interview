#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(limit):
    """ get prime numbers"""
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(2, limit + 1) if primes[i]]


def isWinner(x, nums):
    """ get the winner"""
    def removeMultiples(n):
        """ Remove multiplies """
        primes = sieve_of_eratosthenes(max(nums))
        return [p for p in primes if p in nums]

    winner = "Maria"
    for _ in range(x):
        nums = sorted(nums, reverse=True)
        primes = removeMultiples(nums)

        if len(primes) == 0:
            break

        if winner == "Maria":
            prime = primes[0]
            nums = [num for num in nums if num != prime and num % prime != 0]
        else:
            prime = primes[-1]
            nums = [num for num in nums if num != prime and num % prime != 0]

        if len(primes) > 0:
            winner = "Ben" if winner == "Maria" else "Maria"

    return winner if x > 0 else None
