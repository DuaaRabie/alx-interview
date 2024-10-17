#!/usr/bin/python3
""" Minimum Operations """
import math


def minOperations(n):
    if n <= 0:
        return 0
    
    # Initialize the maximum power of 2
    max_power = 0
    
    # Start from the largest power of 2 (2^63) and go down
    for power in range(63, -1, -1):
        # Check if 2^power doesn't exceed n
        if 2 ** power <= n:
            # Update max_power
            max_power = power
    
    # Return the minimum number of operations
    return max_power if max_power >= 0 else 0
