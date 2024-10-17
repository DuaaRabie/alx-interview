#!/usr/bin/python3
""" Minimum Operations """
import math


def minOperations(n):
    if n <= 0:
        return 0
    
    # Find the position of the leftmost '1' bit
    max_power = 0
    while n:
        n >>= 1
        max_power += 1
    
    return max_power if max_power >= 0 else 0
