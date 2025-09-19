from function import Function
from bisection import find_root
import numpy as np

if __name__=="__main__":

    # Question 1

    # Part a

    function = Function(equation=lambda x: np.exp(-x) - np.sin(x), domain=[0, 1])
    print(f"Problem 1, Part A: {function} has a root at {find_root(function)}.")





