#!/usr/bin/env python3
def summation_i_squared(n):
    """Returns the summation of i^2"""
    if not isinstance(n, (int, float)):
        return None
    else:
        total = int(n*(n + 1)(2*n + 1)/6)
    return total
