import numpy as np
from function import Function

class FixedPointMethod:
    def __init__(self, g: Function):
        self.g = g

    def __call__(self, initial_x: float):
        current_x = initial_x

        while self.g(current_x) != current_x:
            current_x = self.g(current_x)

        return current_x



