#!/usr/bin/env python3
"""probability of x patients who takes drugs will have p side effects."""
import numpy as np


def likelihood(x, n, P):
    "find likelihood of patients taking drugs result in severe side effects."
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or not x >= 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray):
        raise TypeError("P must be a 1D numpy.ndarray")
    if not np.ndim(P) == 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    for value in P:
        if value < 0 or value > 1:
            raise ValueError("All values in P must be in the range [0, 1]")

    # P(x|P) = (n/x)p^x (1-p)^n-x
    # prob of observing patients data x given initial prob of side effects p
    n_factorial = 1
    for i in range(1, n + 1):
        n_factorial *= i
    x_factorial = 1
    for i in range(1, x + 1):
        x_factorial *= i
    nx_factorial = 1
    for i in range(1, n - x + 1):
        nx_factorial *= i
    coefficient = n_factorial / (x_factorial * nx_factorial)
    prob_of_succ = P ** x
    prob_of_failure = (1 - P) ** (n - x)
    likelihood_or_pmf = coefficient * prob_of_succ * prob_of_failure
    return likelihood_or_pmf
