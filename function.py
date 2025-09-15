import matplotlib.pyplot as plt
import numpy as np


class Function:
    def __init__(self, *coefficients, **kwargs):
        if len(coefficients) > 0:
            for coefficient in coefficients:
                self.equation = np.polynomial.Polynomial(coefficients)
        else:
            self.equation = np.polynomial.Polynomial.identity()

    def __eq__(self, other):
        return np.polynomial.Polynomial.__eq__(self.equation, other.equation)

    def __add__(self, other):
        return self.equation

    def __call__(self, *args, **kwargs):
        return self.equation.__call__(*args, **kwargs)
