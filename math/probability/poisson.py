#!/usr/bin/env python3
"""This module creates a class Poisson"""


class Poisson:
    """This class represents a poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """constructor method."""
        self.data = data
        self.lambtha = float(lambtha)
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                Sum = 0
                for i in range(len(data)):
                    Sum += data[i]
            self.lambtha = Sum / len(data)
