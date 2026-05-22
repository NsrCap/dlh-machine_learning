#!/usr/bin/env python
def determinant(matrix):
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

    for j in range(len(matrix)):
        minor = []
        for r in range(1, len(matrix)):
            row = []
            for c in range(len(matrix)):
                if c != j:
                    row.append(matrix[r][c])
            minor.append(row)
        sign = (-1) ** j
        value = matrix[0][j]
        sub_det = determinant(minor)
        det += sign * value * sub_det

return det
