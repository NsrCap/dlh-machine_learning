#!/usr/bin/env python3
"""This module creates a class Normal"""


class Normal:
    """This class represents an normal distribution"""
    # if data is given, the lambtha is calculated from data,
    # else it will be provided by the user, by default lambdha is 1.0
    # simple normal distribution variable v = N(σ (std deviation), μ (mean))
    # σ is std deviation, μ is mean of popultion rather sample
    # ND is symmetric means cut into equal half
    # In ND mean = median = mode
    # pdf ==> f(x) = 1/σ√2π * e ^ −(x−μ)^2 / 2σ^2
    # pdf = how popultion distributed densely around specific value
    # value = continous random variable
    # pdf = likelohood or dansity and not probability
    # for proabability, there is another formula
    # cdf = will be from z-score table
    # cdf accumulated probability from left to x continous random value
    # z-score, used to find area under bell curve for given variable
    # z-score = (x - μ) / σ
    # 68-95-99.7% rule
    # when σ = 1, means move 1 std from mean (left/right)
    # this area under bell curve will represent 68% of population
    # if we travel 2 std.dev from means and so on.......
    # e.g. daily stock returns in USD for one month
    # how likely they are around average is e.g of PDF-ND
    # probabiltiy that returns of stock will be below threshold - CDF
    def __init__(self, data=None, mean=0., stddev=1.):
        """constructor method."""
        # attaching data to object "self or P1, P2 per checker file"
        self.data = data
        self.mean = float(mean)
        self.stddev = float(stddev)
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                total = 0
                for i in range(len(data)):
                    total += data[i]
                average = total / len(data)

                # Variance = ∑ (xi​−μ)^2 / n​
                variance_sum = 0
                for i in range(len(data)):
                    variance_sum += (data[i] - average) ** 2
                variance = variance_sum / len(data)

                # calcuate std deviation = e.g. risk in return of stocks
                stand_deviation = variance ** 0.5
            self.mean = average
            self.stddev = stand_deviation

    def z_score(self, x):
        """calcualte Z-score for given value of x."""
        # normalisation of data
        # z-score = (x - μ) / σ
        # convert real value to standard unit
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        # undo normalisation of data
        # covert back z-score to real value
        # x = μ + zσ
        x = self.mean + z * self.stddev
        return x
