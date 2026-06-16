#!/usr/bin/env python3
"""This module creates a class Normal"""


class Normal:
    """This class represents an normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """constructor method."""
        # if data is given, the lambtha is calculated from data,
        # else it will be provided by the user, by default lambdha is 1.0
        # simple normal distribution variable P(x) = N(σ,μ)
        # σ is std deviation, μ is mean of popultion rather sample
        # ND is symmetric means cut into equal half
        # In ND mean = median = mode
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
        """calcualte x-score for given z-score."""
        # undo normalisation of data
        # this function does not link to z_score method above
        # it is just to understand coversion
        # covert back z-score to real value
        # x = μ + zσ
        x = self.mean + z * self.stddev
        return x

    def pdf(self, x):
        """calcualte dansity function (likelihood) for normal distribution."""
        # pdf ==> f(x) = 1/σ√2π * e ^ −(x−μ)^2 / 2σ^2
        # pdf = how popultion distributed densely around specific value
        # value = continous random variable
        # pdf = likelohood or dansity and not probability
        # for proabability, there is another formula
        # PDF(90) tells how densely stock prices are clustered around 90
        # not the probability of being exactly 90
        # pdf does not tell probability which is area under curve
        π = 3.1415926536
        e = 2.7182818285
        coefficient = 1 / (self.stddev * (2 * π) ** 0.5)
        exponent = e ** (-((x - self.mean) ** 2) / (2 * (self.stddev ** 2)))
        pdf = coefficient * exponent
        return pdf

    def cdf(self, x):
        """calcualte cummulative dist func for normal distribution."""
        # cdf ==> Probability that the variable is less than or equal to x
        # cdf = how much probability has accumulated up to value x
        # value = continous random variable
        # convert value/variable x to z-score value first and then
        # get corresponding value for z-score in table or
        # use erf() function while importing math library
        # this is an error approx function for ND
        # F(x) = 0.5 (1+ erf((σ2​x−μ​)/σ2​))
        # convert into % to understand result
        # stock prices with mean 70, std deviatin 10 and at x=90 price
        # means result z = 2 correspond 0.977 pr 97.7%
        # 97.7% of the stock prices are equal or less than 90USD
        # so there is 2.3% chance, stock prices will be above 90USD
        # Its manipulated z value, added by root sequare two
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))

        # error function, approx error function
        # conver z value to polynomial
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
        # normal curve from inifinty to z and we need 0 to z on x-axis
        return (1 + erf(z)) / 2
