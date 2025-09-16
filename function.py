import numpy as np
from numpy import unsignedinteger


class Function:
    def __init__(self, *coefficients: float, domain= (-(2 ** 16), 2 ** 16)):
        """
        Function takes up to n positional arguments of type float, corresponding to the coefficients of the
        indeterminates of increasing degree, starting from x^0 (i.e., constant). Passing no positional args creates
        the identity polynomial, mapping f(x) = x. Optional keyword argument domain allows restriction of the x domain,
        with the default being from (-2^16, 2^16)
        :param coefficients: float coefficients of the indeterminates, staring from, degree 0 going up.

        """
        self.domain = np.linspace(domain[0], domain[1], 2 ** 20)

        if len(coefficients) > 0:
            for coefficient in coefficients:
                self.equation = np.polynomial.Polynomial(coefficients)
        else:
            self.equation = np.polynomial.Polynomial.identity()

        self.range = self.equation(self.domain)


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

    def set_domain(self, domain: tuple[float, float]):
        self.domain = np.linspace(domain[0], domain[1], 2 ** 20)
        self.calculate()

    def differentiate(self, n: int = 1):
        """
        Return the derivative, if it exists, of order n
        :param n: Order derivative to return Valid for integers values n > 0
        :return: polynomial
        """
        if type(n) is not int or n < 1:
            raise TypeError("integer values greater than 0 only.")

        return self.equation.deriv(n)

    def calculate(self):
        """
        Evaluate the function for all values in the domain. This can take a large amount of time for large domains.
        :return: None
        """
        self.range = self.equation(self.domain)
        return
