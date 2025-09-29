# ./main.py

from fixedpoint import FixedPointMethod
from function import Function
import bisection
import numpy as np
import fixedpoint
# import sys
#
# sys.stdout = open('output.txt', 'w')

def problem_one(*, part_a=True, part_b=True):
    """
    Question 1

    Using the bisection method, find the following:

    Part A: f(x) = e^{-x} - sin{x}
    Find the smallest positive real root

    Part B: f(x) = -1 - 4x + 5x^5
    Fina all real roots

    Keyword Args:
    :part_a: Boolean: should part a be executed. True by default
    :part_b: Boolean: should part b be executed. True by default
    """

    if part_a:
        a = Function(equation=lambda x: np.exp(-x) - np.sin(x), domain=[0, 1], name="exp(-x) - sin(x)")
        a.plot(domain=(0, 4))
        print(f"Problem 1, Part A: {a} has a root at {bisection.find_root(a)}.")

    if part_a:
        b = Function(-1, -4, 0, 0, 0, 1, domain=(-1.5, 1.5))
        print(f"Problem 1, Part B: {b} has roots at: "
              f"{bisection.find_root(b, domain=(-1.5, -1))}, "
              f"{bisection.find_root(b, domain=(-0.5, 0))}, "
              f"{bisection.find_root(b, domain=(1, 1.5))}")

        b.plot()


def problem_three():
    """
    Question 3 Part a

    """
    def g_1(x: float) -> float:
        f = fixedpoint.FixedPointMethod(
            Function(equation=lambda x: x - ((x ** 5 - 7) / (x ** 2)), name="g_1", domain=(0, 15)))
        return f(x)
    def g_2(x: float) -> float:
        f = fixedpoint.FixedPointMethod(
            Function(equation=lambda x: x - (((x ** 5) - 7) / 12), name="g_2", domain=(0, 15)))
        return f(x)
    def g_3(x: float) -> float:
        f = fixedpoint.FixedPointMethod(
            Function(equation=lambda x: x * ((1 + (7 - (x ** 5)) / (x ** 2)) ** 3), name="g_3", domain=(0, 15)))
        return f(x)
    def g_4(x: float) -> float:
        f = fixedpoint.FixedPointMethod(
            Function(equation=lambda x: x - ((x ** 5 - 7) / (5 * (x ** 4))), name="g_4", domain=(0, 15)))
        return f(x)

    print(f"Result of g_1: {g_1(1)}")
    print(f"Last method took {FixedPointMethod.iterations()} steps to complete.")
    print(f"Result of g_2: {g_2(1)}")
    print(f"Last method took {FixedPointMethod.iterations()} steps to complete.")
    print(f"Result of g_3: {g_3(1)}")
    print(f"Last method took {FixedPointMethod.iterations()} steps to complete.")
    print(f"Result of g_4: {g_4(1)}")
    print(f"Last method took {FixedPointMethod.iterations()} steps to complete.")


def problem_four():
    f = Function(equation=lambda x: np.exp(-(x ** 2)), domain=(0, 1), name="exp(-x^2)")

    g = fixedpoint.FixedPointMethod(f)
    f.plot()
    point = g(np.abs(f.domain[0] - f.domain[1]) / 2, tolerance=10 ** (-6))
    print(f"{f} has a fixed point on {f.domain[0], f.domain[1]} at g({point:.5f}) = {f(point):.5f}.")
    print(f"{f} took {FixedPointMethod.iterations()} iterations to complete.")


def problem_five():
    f = Function(equation=lambda x: (4 + (1 / (x ** 2))), name="4 + 1/(x^2)", domain=(3, 5))
    f.plot()
    g = fixedpoint.FixedPointMethod(f)
    point = g(np.abs(f.domain[0] - f.domain[1]), tolerance=2 ** (-64))
    print(f"{f} has a fixed point on {f.domain[0], f.domain[1]} at g({point}) = {f(point)}.")
    print(f"{f} took {FixedPointMethod.iterations()} iterations to complete.")


def problem_six():
    """
    Recall that Newtons method is a fixed point method where

    g(x) = x_n - f'(x_n) (x - x_n)
    """

    def part_a():
        f = Function(-7, 3, -5, 1, domain=(4, 6))

        f_prime = f.derivative()
        print(f_prime)
        g = fixedpoint.FixedPointMethod(Function(equation=lambda x: x - (f(x) / f_prime(x))))

        f.plot()
        point = g(5)
        print(f"{f} has a root on ({f.domain[0], f.domain[1]}) at f({point:.5f}) = {f(point):.5f}.")

    def part_b(guess: float = np.pi):
        f = Function(equation=lambda x: np.tan(x), name="tan(x)", domain=(3, 4))
        f_prime = Function(equation=lambda x: 1 / (np.cos(x) ** 2), name="sec^2(x)", domain=(3, 4))

        g = fixedpoint.FixedPointMethod(Function(equation=lambda x: x - (f(x) / f_prime(x))))

        f.plot()
        point = g(guess)
        print(f"Initial Guess: {guess}")
        print(f"{f} has a root on ({f.domain[0], f.domain[1]}) at f({point:.5f}) = {f(point):.5f}.")
        print(f"Number of iterations: {g.iterations()}")

    part_a()
    part_b()


def problem_eight():
    def part_ab():
        f = Function(-8, 0, 1, domain=(2, 3))
        f_prime = f.derivative()
        f_very_prime = f_prime.derivative()
        g = fixedpoint.FixedPointMethod(Function(equation=lambda x: x - (f(x) / f_prime(x))))

        newton = g(3, tolerance=10 ** (-6))

        f.plot()
        print(f"{f} has a root on {f.domain} at f({newton:.5f}) = {f(newton):.5f}.")
        print(f"Newton's method took {FixedPointMethod.iterations()} iterations to complete.")

        g = fixedpoint.FixedPointMethod(
            Function(equation=lambda x: x
                                        - (
                                            f(x) / f_prime(x)
                                        )
                                        * (1
                                           - (f(x) * f_very_prime(x))
                                           / (2 * (f_prime(x) ** 2))
                                           ) ** (-1)
                     ))
        hailey = g(3, tolerance=10 ** (-6))

        print(f"{f} has a root on {f.domain} at f({hailey:.5f}) = {f(hailey):.5f}.")
        print(f"Hailey's method took {FixedPointMethod.iterations()} iterations to complete.")

    part_ab()


if __name__ == "__main__":
    print("Problem 1:")
    problem_one()
    print("\n\n")
    print("Problem 3:")
    problem_three()
    print("\n\n")
    print("Problem 4:")
    problem_four()
    print("\n\n")
    print("Problem 5:")
    problem_five()
    print("\n\n")
    print("Problem 6:")
    problem_six()
    print("\n\n")
    print("Problem 8")
    problem_eight()
    pass
