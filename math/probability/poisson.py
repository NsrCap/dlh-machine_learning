#!/usr/bin/env python3
"""This module creates a class Poisson"""


class Poisson:
    """This class represents a poisson distribution"""
    # if data is given, the lambtha is calculated from data,
    # else it is given by the user, by default it is 1.0
    # lambtha is the expected number of occurrences in a given time frame
    def __init__(self, data=None, lambtha=1.):
        """constructor method."""
        # attaching data to object "self or P1, P2 per checker file"
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
    # self is the same object as above and below in pmf function,
    # it is used to access the attributes of the object
    # object attributes are data & lambtha, attached to object in constructor
    # k is method parameter/input, not an object attribute
    # k is temporary variable used to calculate PMF
    # it is not attached to self because it is not needed outside the method
    # if needed outside the method
    # it can be returned/passed as an argument to class/another method
    # using self.k = k which will attach k to the object
    # however, this is not required per this task
    # attaching k means that it will be accessible as attribute of object
    # or simply it means storing data, lanbtha, k in object for later use
    # pmf is a method or reusable behavior of the object
    # k is specific number events that occur in a given time frame

    def pmf(self, k):
        """Calculate PMF for a given number of “successes”"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        else:
            # calculate PMF using the formula: (e^-lambtha * lambtha^k) / k!
            e = 2.7182818285
            factorial = 1
            for i in range(1, k + 1):
                factorial *= i
            pmf = (e ** (-self.lambtha) * (self.lambtha ** k)) / factorial
            return pmf
