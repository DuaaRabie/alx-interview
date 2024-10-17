#!/usr/bin/python3
""" Minimum Operations """
import math


def minOperations(n):
    """ min Operations function """
    if n <= 0:
        return 0
    
    # Calculate log_2(n) and round up to get the smallest power of 2 >= n
    k = math.ceil(math.log2(n))
    
    # Check if this power of 2 equals n
    return k if (1 << k) - 1 == n else 0
