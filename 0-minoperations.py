#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    if n == 0:
        return 0
    
    operations = 0  # Initial copy operation
    
    # Loop through powers of 2 up to n
    power_of_two = 2
    while power_of_two <= n:
        operations += 1  # Add paste operation
        power_of_two *= 2
    
    return operations + 1
