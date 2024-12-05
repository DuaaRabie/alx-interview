#!/usr/bin/python3
""" Rotate 2d matrix module """


def rotate_2d_matrix(matrix):
    """ rotate a 2 dimention matrix """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
    return matrix