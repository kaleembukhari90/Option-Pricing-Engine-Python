# Implemented all global functions

from scipy.stats import norm

def N(x):
    """Cumulative distribution function (CDF) of the standard normal distribution."""
    return norm.cdf(x, 0.0, 1.0)

def n(x):
    """Probability density function (PDF) of the standard normal distribution."""
    return norm.pdf(x, 0.0, 1.0)