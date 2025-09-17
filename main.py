from function import Function
from bisection import find_root

if __name__=="__main__":
    a = Function(0, -2, 1, domain=(1, 4))
    a.plot()

    print(f"Root at {find_root(a)}.")




