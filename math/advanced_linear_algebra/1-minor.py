#!/usr/bin/env python3
"""Module that calculates the minor of a matrix."""


def determinant(matrix):
    """Calculates the determinant of a matrix."""

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(len(matrix)):
        smaller = []
        for r in range(1, len(matrix)):
            small_row = []
            for c in range(len(matrix)):
                if c != j:
                    small_row.append(matrix[r][c])
            smaller.append(small_row)
        sign = (-1) ** j
        det += sign * matrix[0][j] * determinant(smaller)
    return det


def minor(matrix):
    """Calculates the minor matrix of a matrix."""

    # check matrix type
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
    minor_matrix = []
    # loop over each row index i → build each row of minor matrix (Result)
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            # loop over each column index j → compute each value for row
            # which value → require determinant of each element
            # create smaller matrix to get determinant as valueforminormatrix
            smaller = []
            # loop over rows of original matrix → pick rows except i
            for r in range(len(matrix)):
                if r == i:
                    continue
                small_row = []
                # loop over columns of original matrix → pick columns except j
                for c in range(len(matrix)):
                    if c == j:
                        continue
                    # take element from original matrix
                    small_row.append(matrix[r][c])
                smaller.append(small_row)
            # get determinant of smaller matrix
            row.append(determinant(smaller))
        minor_matrix.append(row)
    return minor_matrix
