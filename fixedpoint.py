import numpy as np
from function import Function



class FixedPointMethod:
    __iterations: int = 0
    def __init__(self, g: Function):
        self.g = g

    def __call__(self, initial_x: float, *, tolerance: float = 2 ** (-16)):
        current_x = initial_x
        FixedPointMethod._FixedPointMethod__iterations = 0
        try:
            while np.abs(self.g(current_x) - current_x) > tolerance:
                current_x = self.g(current_x)
                FixedPointMethod._FixedPointMethod__iterations += 1
        except OverflowError:
            return OverflowError(f"{self.g} diverged from initial value {initial_x}")
        except Exception as e:
            raise e
        return current_x

    @staticmethod
    def iterations() -> int:
        """
        Gets the number of iterations taken by the last called fixed point background
        :return:
        """
        return FixedPointMethod._FixedPointMethod__iterations





