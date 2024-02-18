"""
Combinatoric Selections
"""


def factorial(num):
    """
    this finds factorial of a num
    """
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


def answer():
    """
    How many, not necessarily distinct, values of n!/r!(n-r)!
    for 1<=n<=100
    are greater than one-million?
    """
    for n in range(100):
        c = 0
        for r in range(100):
            ans = factorial(n) / (factorial(n - r) * factorial(r))
            if ans > 1000000:
                c += 1

    return c


if __name__ == "__main__":
    print(answer())
