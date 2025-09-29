# ./bisection.py

import numpy as np
from function import Function

def find_root(f: Function, *, domain: tuple[float, float] = None, tolerance: float = 2 ** -48):
    if domain is None:
        domain = f.domain

    neg_endpoint = domain[0] if f(domain[0]) < 0 else domain[1]
    pos_endpoint = domain[0] if f(domain[0]) > 0 else domain[1]

    while (np.abs(pos_endpoint - neg_endpoint)) > tolerance:
        midpoint = (pos_endpoint + neg_endpoint) / 2

        if f(midpoint) == 0: return midpoint

        if f(midpoint) < 0:
            neg_endpoint = midpoint
        else:
            pos_endpoint = midpoint

    return (pos_endpoint + neg_endpoint) / 2


