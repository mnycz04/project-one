from function import Function
import bisection
import numpy as np
import fixedpoint


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

    g_1 = fixedpoint.FixedPointMethod(
        Function(equation=lambda x: x - (((x ** 5) - 7) / (x ** 2)), name="g_1", domain=(-5, 5)))
    g_2 = fixedpoint.FixedPointMethod(
        Function(equation=lambda x: x - (((x ** 5) - 7) / 12), name="g_2", domain=(-5, 5)))
    g_3 = fixedpoint.FixedPointMethod(
        Function(equation=lambda x: x * ((1 + (7 - (x ** 5)) / (x ** 2)) ** 3), name="g_3", domain=(-5, 5)))
    g_4 = fixedpoint.FixedPointMethod(
        Function(equation=lambda x: x - ((x ** 5 - 7) / 5 * (x ** 4)), name="g_4", domain=(-5, 5)))

    print(g_1(1))
    print(g_2(1))
    print(g_3(1))
    print(g_4(1))


if __name__ == "__main__":
    # problem_one()

    problem_three()
