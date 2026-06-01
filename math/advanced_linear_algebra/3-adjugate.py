#!/usr/bin/env python3
"""Module that calculates the cofactor of a matrix."""


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
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            # build smaller matrix by removing row i and column j
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
            # get determinant of smaller matrix
            row.append(determinant(smaller))
        minor_matrix.append(row)
    return minor_matrix


def cofactor(matrix):
    """Returns the cofactor of a matrix."""

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if len(row) != len(matrix) or matrix == [[]]:
            raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1:
        return [[1]]

    cofact_matrix = []
    min_matrix = minor(matrix)
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append((-1) ** (i + j) * min_matrix[i][j])
        cofact_matrix.append(row)
    return cofact_matrix


def adjugate(matrix):
    """Returns the adjugate of a matrix"""

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if len(row) != len(matrix) or matrix == [[]]:
            raise ValueError("matrix must be a non-empty square matrix")

    adjugate_matrix = []
    cof_matrix = cofactor(matrix)
    for j in range(len(cof_matrix)):
        row = []
        for i in range(len(cof_matrix)):
            row.append(cof_matrix[i][j])
        adjugate_matrix.append(row)
    return adjugate_matrix