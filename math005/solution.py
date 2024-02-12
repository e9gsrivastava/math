""" to find the smallest number that is divisible by given  trange that is p,q"""


def solver(p, q):
    """this is the function to perform above functionality"""

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    s = 1
    for i in range(min(p, q), max(p, q) + 1):
        s = (i * s) / gcd(s, i)
    return int(s)


def answer():
    """this is the function to perform above functionality"""
    p = 1
    q = 20

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    s = 1
    for i in range(min(p, q), max(p, q) + 1):
        s = (i * s) / gcd(s, i)
    return int(s)


if __name__ == "__main__":
    print(answer())
    print(solver(11, 2))
