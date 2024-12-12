#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """get a list of primes up to 10000 using the Sieve of Eratosthenes"""
    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0], primes[1] = False, False
        for i in range(2, int(limit ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, limit + 1, i):
                    primes[j] = False
        return [i for i in range(2, limit + 1) if primes[i]]

    # Generate all primes up to 10000
    max_n = 10000
    primes_up_to_max = sieve_of_eratosthenes(max_n)

    def play_game(n):
        """Function to simulate the game for a given n"""
        if n == 1:
            return "Ben"  # Maria cannot play, so Ben wins
        # Create the list of numbers from 1 to n
        # True means the number is still in the game
        numbers = [True] * (n + 1)

        # Count of rounds won
        turn = 0  # 0 for Maria's turn, 1 for Ben's turn

        # Simulate the game
        for prime in primes_up_to_max:
            if prime > n:
                break
            # If the prime is still available to be picked
            if numbers[prime]:
                # Player picks this prime
                for multiple in range(prime, n + 1, prime):
                    # Remove the prime and its multiples
                    numbers[multiple] = False
                # Alternate turns between Maria and Ben
                turn = 1 - turn

        # If turn is 0 after the loop,
        # then Ben couldn't make a move, and Maria wins
        if turn == 0:
            return "Maria"
        else:
            return "Ben"

    # Count the wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    # Determine who has the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
