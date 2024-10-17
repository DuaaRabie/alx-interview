#!/usr/bin/python3
""" Minimum Operations """
import math


def minOperations(n):
    """ min Operations function """
    if n <= 0:
        return 0

    # Convert n to binary and remove the '0b' prefix
    bin_n = bin(n)[2:]

    # Find the position of the leftmost '1'
    max_power = len(bin_n) - 1 - bin_n.rfind('1')

    return max_power if max_power >= 0 else 0
