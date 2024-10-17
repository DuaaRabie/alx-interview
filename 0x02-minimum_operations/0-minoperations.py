#!/usr/bin/python3
""" Minimum Operations """
import math


def minOperations(n):
    if n <= 0:
        return 0
    
    factor = 2
    operations = 0

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
