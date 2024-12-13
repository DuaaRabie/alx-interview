#!/usr/bin/python3
"""Prime Game"""
from typing import List


def sieve_of_eratosthenes(n):
    """ get prime numbers:
    Create a boolean array
    "prime[0..n]" and initialize
    all entries it as true.
    A value in prime[i] will
    finally be false if i is
    Not a prime, else true. """
    prime = [True for i in range(n+1)]
    prime[0], prime[1] = False, False
    p = 2
    while (p * p <= n):
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] is True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if prime[p]]


def isWinner(x: int, nums: List[int]) -> str:
    """ get return winner Ben or Maria or None"""
    if nums is None:
        return None
    if x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0
    # counts the turns
    nums = nums[:x]
    # loop in the nums
    for n in nums:
        if n == 1:
            ben_wins += 1
            continue
        if n <= 0:
            continue

        numbers_primes = sieve_of_eratosthenes(n)
        remaining = list(range(1, n + 1))
        current_player = "Maria"
        # loop in the range
        while remaining:
            for prime in numbers_primes:
                if prime in remaining:
                    remaining = [num for num in remaining if num % prime != 0]
                    if current_player == "Maria":
                        current_player = "Ben"
                    else:
                        current_player = "Maria"
            else:
                if current_player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
