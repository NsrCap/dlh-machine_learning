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

    for row in matrix:
        for value in row:
            if isinstance(value, list):
                raise TypeError("matrix must be 2D not 3D")

    # base case
    if len(matrix) == 1:
        return [[1]]

    # check square
    for row in matrix:
        if len(row) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")

    minor = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            # build smaller matrix by removing row i and column j
            smaller = []
            for r in range(len(matrix)):
                if r == i:
                    continue
                else:
                    small_row = []
                    for c in range(len(matrix)):
                        if c == j:
                            continue
                        small_row.append(matrix[r][c])
                    smaller.append(small_row)
                row.append(smaller)
            minor.append(row)
    return minor
