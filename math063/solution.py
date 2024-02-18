"""
Powerful Digit Counts
"""


def answer():
    """
    How many n-digit positive
    integers exist which are also an
    nth power?
    """
    c = 0
    for i in range(1, 10):
        j = 1
        while len(str(i**j)) == j:
            c += 1
            j += 1
    return c


if __name__ == "__main__":
    print(answer())
