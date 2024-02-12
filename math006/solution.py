"""this is maths006"""


def answer(n):
    """this finds the the difference between the sum of the squares of the first ten natural numbers and the square of the sum"""
    n = n
    s = ((n) * (n + 1) * (2 * n + 1)) / 6
    sl = ((n * (n + 1)) / 2) ** 2
    return sl - s


def solver(start, end):
    """this finds the the difference between the sum of the squares of the first ten natural numbers and the square of the sum"""

    s = ((end) * (end + 1) * ((2 * end) + 1)) / 6 - (
        ((start) * (start + 1) * ((2 * start) + 1)) / 6
    )
    sl = (((end * (end + 1)) / 2) - ((start * (start + 1)) / 2)) ** 2

    return sl - s


if __name__ == "__main__":
    print(int(solver(0, 100000000)))
    print(int(answer(100)))
