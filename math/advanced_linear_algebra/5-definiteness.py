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


def definiteness(matrix):