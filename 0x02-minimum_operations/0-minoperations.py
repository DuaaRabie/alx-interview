#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ min Operations function """
    k = 0
    while (1 << k) - 1 < n:
        k += 1
    
    return k if (1 << k) - 1 == n else 0
