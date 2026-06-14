#!/usr/bin/env python3
"""This module creates a class exponential"""


class Exponential:
    """This class represents an exponential distribution"""
    # if data is given, the lambtha is calculated from data,
    # else it will be provided by the user, by default it is 1.0
    # lambtha is the rate of no of event over time
    # while waiting time = 1/λ for exponential SF
    # time matter in this distribution, its a continous random variable
    # e.g. waiting time for call, bus, failure,increase
    # so your waiting for the next event to happens
    # that why decay (-lambdha in exponent) matters in probability
    # becuase time will get decrease when we start waiting for event
    # whats the probability that next emails will arive in 10mins
    # lambdha = 5 emails (Event) / next hour (time)
    # finance. e.g. time btw no of trades, time btw credit default
    # how long next default will occure
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
            self.lambtha = 1 / (Sum / len(data))
