"""this is used to solve ssum of odd even  """


def solver(start, end, even=False, odd=False):
    # x=1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    """this func solves  odd or even sum based on condition"""

    l = []
    a = 1
    b = 2

    while a <= end:
        l.append(a)

        a, b = b, a + b
    so = 0
    se = 0
    if start > end:
        return None

    for i in l:
        if i % 2 == 0 and i > start:
            se += i
        elif i % 2 != 0 and i > start:
            so += i
    if even is True and odd is True:
        return se, so
    if odd is True and even is False:
        return so, se
    if odd is True and even is False:
        return so, se

    return None


def answer():
    """this is to solve"""
    a = 1
    b = 2
    s = 0
    while a <= 4000000:
        if a % 2 == 0:
            s += a
        a, b = b, a + b

    return s


if __name__ == "__main__":
    print(answer())
    print(solver(10, 10000, even=False, odd=True))
