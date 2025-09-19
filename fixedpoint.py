import numpy as np
from function import Function

class FixedPointMethod:
    def __init__(self, g: Function):
        self.g = g

    def __call__(self, initial_x: float, *, tolerance: float = 2 ** (-16)):
        current_x = initial_x
        try:
            while np.abs(self.g(current_x) - current_x) > tolerance:
                current_x = self.g(current_x)
        except OverflowError:
            return OverflowError(f"{self.g} diverged from initial value {initial_x}")
        except Exception as e:
            raise e
        return current_x



