#!/usr/bin/env python3
"""Module that calculates the minor of a matrix."""


def minor(matrix):
    """Calculates the minor of a matrix."""

    # check matrix type including rows
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

    # check 2D not 3D
    for row in matrix:
        for value in row:
            if isinstance(value, list):
                raise TypeError("matrix must be a list of lists")

    # check empty
    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    # check square
    for row in matrix:
        if len(row) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")

    # base case
    if len(matrix) == 1:
        return [[1]]

    # build minor matrix
    minor = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            smaller = []
            for r in range(len(matrix)):
                if r == i:
                    continue
                small_row = []
                for c in range(len(matrix)):
                    if c == j:
                        continue
                    small_row.append(matrix[r][c])
                smaller.append(small_row)
            row.append(smaller)
        minor.append(row)
    return minor
