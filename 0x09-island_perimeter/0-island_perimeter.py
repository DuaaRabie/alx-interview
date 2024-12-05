#!/usr/bin/python3
""" 0. Island Perimeter """


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid"""
    perimeter = 0
    prev_row_land = []
    current_row_land = []
    for index, row in enumerate(grid):
        prev_element = 0
        for inner_index, element in enumerate(row):
            if element == 1:
                current_row_land.append(inner_index)
                if prev_element == 0 or inner_index == 0:
                    perimeter += 1
                if inner_index not in prev_row_land:
                    perimeter += 1
                if inner_index == len(row) + 1:
                    perimeter += 1
                if inner_index < len(row) - 1:
                    if row[inner_index + 1] == 0:
                        perimeter += 1
                if index == 0:
                    perimeter += 1
                if not prev_row_land and not index:
            else:
                if inner_index in prev_row_land:
                    perimeter += 1
            prev_element = element
        prev_row_land = current_row_land[:]
        current_row_land = []
    return perimeter
