#!/usr/bin/python3
""" Minimum Operations """
import math


def minOperations(n):
    # Handle edge cases
    if n <= 0:
        return 0
    
    # Create a dictionary to store memoized results
    memo = {}
    
    def dp(current_chars, current_ops):
        # Base case: if we've reached the target or exceeded it
        if current_chars == n or current_chars > n:
            return current_ops
        
        # Check if we've already solved this subproblem
        if (current_chars, current_ops) in memo:
            return memo[(current_chars, current_ops)]
        
        # Try both Copy All and Paste operations
        copy_all = dp(current_chars * 2, current_ops + 1)
        paste = dp(current_chars + current_chars, current_ops + 1)
        
        # Store the result in memo
        memo[(current_chars, current_ops)] = min(copy_all, paste)
        
        return memo[(current_chars, current_ops)]

    # Start with 0 characters and 0 operations
    return dp(1, 0)
