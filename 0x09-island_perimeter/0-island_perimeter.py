#!/usr/bin/python3
""" 0. Island Perimeter """


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the top boundary
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the bottom boundary
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the left boundary
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the right boundary
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
