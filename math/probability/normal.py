#!/usr/bin/env python3
"""This module creates a class exponential"""


class Normal:
    """This class represents an exponential distribution"""
    # if data is given, the lambtha is calculated from data,
    # else it will be provided by the user, by default lambdha is 1.0
    # simepl exponential function = f(x) = e^x
    # exponential function in decay form, time involve
    # f(x) = e^λx or f(t) = e^-λt
    # lambtha is the rate of events occure for given time
    # while λ is rate paraemter and is λ = 1/mean for exponential. DF
    # time matter in this distribution, its a continous random variable
    # e.g. waiting time for call, bus, failure, accident
    # focus is to find probabiltiy of waiting time untill next event
    # that why decay used (-lambdha in exponent) in Exp.Dist.Func.
    # becuase possibility of still wating will get decrease over time
    # probability of time itslef will not decrease as time passes
    # probability that next emails will arive in 10mins = not possible
    # becuase time is continous random variable and probability of
    # time itself at specific point in time in future is not possible
    # whats the probability that next emails will arive within 10mins = CDF
    # core concept difference is waiting time vs time
    # finance. e.g. prob of time btw no of trades, of time btw credit default
    # how long it will take that next trade/default will occure
    # find probability of waiting time for given interval of time
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
            # lambdha = 1/mean for exponential DF
            self.lambtha = 1 / (Sum / len(data))

    def pdf(self, x):
        """find PDF where dansity=likelihood for give time period."""
        # PDF for exponential = f(x) = λ.e^-λt
        # PDF will just confirm likelihood rather probabiltiy of waiting time
        # actual probability for Exp.D.F will come from area under curve
        # see integration formula P(a< T < b) = ∫^ab ​f(t)dt
        # how likely the event is to occur around a specific time (density)
        # but not the actual probability.
        if x < 0:
            return 0
        else:
            # calculate PDF using the formula: (lambdha * e^-lambtha.Time)
            e = 2.7182818285
            prob_dist_func = ((self.lambtha) * e ** ((-self.lambtha) * x))
            return prob_dist_func

    def cdf(self, x):
        """find CDF for give time period."""
        # Probability that event occurs within time t or x
        # e.g. whats the probability that next emails will arive within 10mins
        # the probability that the event has occurred up to a given time
        if x < 0:
            return 0
        else:
            # calculate PDF using the formula: (lambdha * e^-lambtha.Time)
            e = 2.7182818285
            cum_dist_func = 1 - e ** ((-self.lambtha) * x)
            return cum_dist_func
