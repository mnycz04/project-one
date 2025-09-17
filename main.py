from function import Function
from bisection import find_root
import numpy as np

if __name__=="__main__":
    a = Function(equation=lambda x: np.exp(-x) - np.sin(x), domain=(0, 3))
    a.plot()
    print(f"Function a has a root at {find_root(a)}.")





