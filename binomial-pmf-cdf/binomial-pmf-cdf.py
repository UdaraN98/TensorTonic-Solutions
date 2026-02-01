import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    def _pmf(n,p,k):
        return float(comb(n,k)*(p**k)*((1-p)**(n-k)))
    cdf = 0
    i = 0
    while i <= k:
        cdf += _pmf(n,p,i)
        i+=1

    return _pmf(n,p,k), cdf