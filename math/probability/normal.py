#!/usr/bin/env python3
"""This module creates a class Normal"""


class Normal:
    """This class represents an normal distribution"""
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
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """calcualte x-score for given z-score."""
        x = self.mean + z * self.stddev
        return x

    def pdf(self, x):
        """calcualte dansity function for normal distribution."""
        π = 3.1415926536
        e = 2.7182818285
        coefficient = 1 / (self.stddev * (2 * π) ** 0.5)
        exponent = e ** (-((x - self.mean) ** 2) / (2 * (self.stddev ** 2)))
        pdf = coefficient * exponent
        return pdf

    def cdf(self, x):
        """calcualte cummulative dist func for normal distribution."""
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))

        def erf(x):
            π = 3.1415926536
            erf = (2 / (π ** 0.5)) * (
                x
                - (x ** 3) / 3
                + (x ** 5) / 10
                - (x ** 7) / 42
                + (x ** 9) / 216
            )
            return erf
        return (1 + erf(z)) / 2
