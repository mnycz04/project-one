from function import Function
from bisection import find_root
import numpy as np

if __name__=="__main__":

    # Question 1
    # Part a

    function = Function(equation=lambda x: np.exp(-x) - np.sin(x), domain=[0, 1])
    function.plot(domain=(0, 4))
    print(f"Problem 1, Part A: {function} has a root at {find_root(function)}.")

    # Part b

    function = Function(-1, -4, 0, 0, 0, 1, domain=(-1.5, 1.5))
    print(f"Problem 1, Part B: {function} has roots at: " 
          f"{find_root(function, domain=(-1.5, -1))}, " 
          f"{find_root(function, domain=(-0.5, 0))}, " 
          f"{find_root(function, domain=(1, 1.5))}")

    function.plot()

    # Question 3

    g =  [Function(equation=lambda x: x - (((x**5) - 7) / (x**2)), name="g_1" ),
          Function(equation=lambda x: x - (((x**5) - 7) / 12), name="g_2"),
          Function(equation=lambda x: x * ((1 + (7 - (x**5)) / (x**2))**3) , name="g_3"),
          Function(equation=lambda x: x - ((x**5 - 7) / 5 * (x**4)), name="g_4") ]

    for func in g:
        func.plot(domain=(-10, 10))






