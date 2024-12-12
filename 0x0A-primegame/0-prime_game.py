#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(n):
    """ get prime numbers:
    Create a boolean array
    "prime[0..n]" and initialize
    all entries it as true.
    A value in prime[i] will
    finally be false if i is
    Not a prime, else true. """
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] is True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime


def isWinner(x, nums):
    """ get the winner"""
    primes = sieve_of_eratosthenes(max(nums))
    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        remaining = set(nums)
        while remaining:
            if len(remaining) == 1:
                chosen = list(remaining)[0]
                removed = {chosen}
                break

            prime = min(remaining)
            if prime not in primes:
                prime = next((p for p in primes if p > prime), None)

            removed = set()
            for num in remaining:
                if num % prime == 0:
                    removed.add(num)

            remaining -= removed

        if len(remaining) == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        None
