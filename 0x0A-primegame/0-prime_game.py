#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    def isPrime(n):
        """ get prime numbers """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def removeMultiples(n):
        """ remove multiplications """
        primes = []
        for num in nums:
            if isPrime(num):
                primes.append(num)
        return primes

    winner = "ben"

    for _ in range(x):
        nums = sorted(nums, reverse=True)
        primes = removeMultiples(nums)

        if len(primes) == 0:
            break

        if winner == "Maria":
            prime = primes.pop(0)
            nums = [num for num in nums if num != prime and num % prime != 0]
        else:
            prime = primes[0]
            nums = [num for num in nums if num != prime and num % prime != 0]

        if len(primes) > 0:
            winner = "Ben" if winner == "Maria" else "Maria"

    return winner if x > 0 else None
