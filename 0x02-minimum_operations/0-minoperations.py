#!/usr/bin/python3
""" Minimum Operations """
import math


def minOperations(n):
    """ min Operations function """
    if n <= 0:
        return 0

    # Calculate LCM of powers of 2 until we reach or exceed n
    k = 0
    while True:
        lcm_value = math.lcm(2**k, 2**(k+1))
        if lcm_value >= n:
            break
        k += 1

    # Check if this LCM equals n
    return k if lcm_value == n else 0
