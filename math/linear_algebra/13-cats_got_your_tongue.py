#!/usr/bin/env python3
"""this task isto perform cancatenation on matrix."""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """this is documentation to doing cancatenation of matrix."""
    new_matrix = np.concatenate((mat1, mat2, axis=axis))
    return new_matrix
