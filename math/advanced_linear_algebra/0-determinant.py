#!/usr/bin/env python3
"""Module that calculates the determinant of a matrix."""


def determinant(matrix):
    """Calculates the determinant of a matrix."""

    # check matrix type including rows
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

    # special case
    if matrix == [[]]:
        return 1

    # check square
    for row in matrix:
        if len(row) != len(matrix):
            raise ValueError("matrix must be a square matrix")

    # base case
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        return a*d - b*c

    # recursive case
    det = 0

    # move across column of row 0, pick each element
    for j in range(len(matrix)):
        smaller_matrix = []
        sign = (-1) ** j
        value = matrix[0][j]
        # loop over remaining rows (r), strat from row 1 and move till end
        for r in range(1, len(matrix)):
            row = []
            # move column by column (c) for each rows starting from 1
            for c in range(len(matrix)):
                # if col idx matches col we are moving in top row (j), skip it
                if c != j:
                    row.append(matrix[r][c])
            smaller_matrix.append(row)

        # function is calling itself before user call after codes end at return
        recursion = determinant(smaller_matrix)
        det += sign * value * sub_det

    return det
