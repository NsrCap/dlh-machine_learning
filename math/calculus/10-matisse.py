#!/usr/bin/env python3
"""Module calculates the derivative of polynomial"""


def poly_derivative(poly):
    """this is documentation to finding coefficient list of polynomial."""

    if not isinstance(poly, list) or len(poly) == 0:
        return None
    for element in poly:
        if not isinstance(element, (int, float)):
            return None

    # base case derivative, like for constant its zero
    if len(poly) == 1:
        return [0]

    # derivative of function above constant
    new_poly = []
    for i in range(1, len(poly)):
        new_poly.append(i * poly[i])
    return new_poly
