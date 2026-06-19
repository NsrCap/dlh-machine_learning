#!/usr/bin/env python3
"""probability of x patients who takes drugs will have p side effects."""
# bayesian prob follow baye's theoram which is
# to equate conditional probability of both events togather
# conditional prob formula to find prob of desired outcome
# condition prob means one event already occure and
# find prob of another event given first event prob
# P(A|B) = P(A ∩ B)/ P(B)
# P(B|A) = P(A ∩ B)/ P(A)
# P(A ∩ B) = P(A and B) = join prob = prob of both event occuring
# P(B) = Prob of event already occured and this must be > 0
# otherwise undefined result = invalid assessment
# conditional prob != bayes theoram rahter
# its rearranging/subtitute nominator of conditional prob
# Nominator in both are same P(A ∩ B), so we can equate
# P(A|B)P(A) = P(B|A)P(B)
# P(A|B) = P(B|A)P(A) / P(B) = bayes theorem or
# x = data of patient and P = prob of side effects
# P(P|data) = P(data|P).P(P) / P(data)
# in above formula:
# P(A/B) = posterior prob
# P(B/A) or P(data|p) = Likelihood = (updated info)
# P(A) = initial prob = uniform prior = prior dist = Beta Dist
# P(B) = Prob of B in all possible events
import numpy


def likelihood(x, n, P):
    "find likelihood of patients taking drugs result in severe side effects."
    # x = data, and observe change in data and update P
    # as P become random variable like x=k value
    # P is continous(float) while x=k are still discrete (whole no.)
    # as we updated our belief about P value, so cond. Prob. needed
    # cond. prob needed when 1. x & p outcome/events are dependent or
    # 2. when we update our inital belief about variable or parameter
    # P(A∩B) = P(B|A) . P(A) ==> dependent event prob. rearrange it
    # P(B|A) = P(A∩B) / P(A), this P(B|A) is likelihood func. in Baye's theorem
    # P(B|A) = Binomial formula (n/x)p^x (1-p)^n-x
    # A = P (prob of side effects) & B = data of patients (x=k value)
    # P(x|P) = P(x∩P)/P(P) = pmf of BD = (n/x)p^x (1-p)^n-x
    # P(x∣P) is the probability of observing data given p
    # this given p value menas, initial p value lets say 0.5
    # repeat n=5 trials, 3 heads and 2 tails → this is data x=k=3
    # initially we may assume p ≈ 0.5 (prior belief)
    # after observing data (3/5), we update our belief about p
    # the data suggests p could be around 0.6, but not exactly equal to 0.6
    if not n > 0:
        raise ValueError("the message n must be a positive integer")
    if not x >= 0:
        raise ValueError("x must be an integer and greater than or == 0")
    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, numpy.ndarray):
        raise TypeError("P must be a 1D numpy.ndarray")
    if not numpy.ndim(P) == 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    for value in P:
        if value < 0 or value > 1:
            raise ValueError("All values in P must be in the range 0 & 1")

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
