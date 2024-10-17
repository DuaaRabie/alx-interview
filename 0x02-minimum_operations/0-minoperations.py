#!/usr/bin/python3
""" Minimum Operations """
import math


def minOperations(n):
    if n <= 0:
        return 0

    chars = 1
    operations = 0

    while chars < n:
        if chars % n == 0:
            operations += 2
            copied = chars * 2
        else:
            operations += 1
            copied = chars + 1
        
        chars = copied

    return operations
