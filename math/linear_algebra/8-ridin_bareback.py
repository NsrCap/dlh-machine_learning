#!/usr/bin/env python3
"""this task isto perform 2D matrix multiplication."""


def mat_mul(mat1, mat2):
    """this is documentation for matrix multiplication."""

    if len(mat1[0]) != len(mat2):
        return None

    result_mat = []

    for i in range(len(mat1)):
        row = []
        for k in range(len(mat2[0])):
            P = 0  # initialise sum after multiplication
            for j in range(len(mat2)):
                x = mat1[i][j] * mat2[j][k]
                P += x
            row.append(P)
        result_mat.append(row)

    return result_mat
