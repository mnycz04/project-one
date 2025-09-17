import matplotlib.pyplot as plt
import numpy as np


class Function:
    def __init__(self, *coefficients, equation=None, domain=(-(2**10), (2**10))):
        if equation is not None:
            self.equation = equation
        elif len(coefficients) > 0:
            self.equation = np.polynomial.Polynomial(coefficients)
        else:
            self.equation = np.polynomial.Polynomial.identity()

        self.domain = domain

    def __eq__(self, other):
        return np.polynomial.Polynomial.__eq__(self.equation, other.equation)

    def __add__(self, other):
        return self.equation.__add__(other.equation)

    def __radd__(self, other):
        return self.equation.__radd__(other.equation)

    def __sub__(self, other):
        return self.equation.__sub__(other.equation)

    def __call__(self, *args, **kwargs):
        return self.equation.__call__(*args, **kwargs)

    def __str__(self):
        return self.equation.__str__()

    def plot(self):
        x_vals = np.linspace(self.domain[0], self.domain[1], 10 * (self.domain[1] - self.domain[0]))
        y_vals = self(x_vals)

        plt.plot(x_vals, y_vals)
        plt.grid(True)
        plt.show()
        return

    def derivative(self, n: int = 1):
        if type(n) is not int or n < 0:
            return TypeError("n must be a positive integer")
        else:
            return self.equation.deriv(n)


