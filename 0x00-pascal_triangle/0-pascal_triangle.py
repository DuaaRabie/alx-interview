#!/usr/bin/python3
"""
pascal_triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    Args:
    n (int): The number of rows in the triangle.

    Returns:
    list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    result = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = result[i-1]
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)
        result.append(row)

    return result
