"""to find highest palindrome of n digit """


def answer():
    """this finds palindrome"""
    result = 0
    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, i + 1)):
            a = str(i * j)
            if a == a[::-1]:
                if result < i * j:
                    result = i * j

    return result


def solver(n, p=None, q=None):
    """this finds palindrome"""
    result = 0
    a = 10 ** (n - 1)
    if q is None:
        for i in reversed(range(a, p + 1)):
            for j in reversed(range(a, i + 1)):
                a = str(i * j)
                if a == a[::-1]:
                    if result < i * j:
                        result = i * j
        return result
    if p is not None and q is not None:
        for i in reversed(range(p, q + 1)):
            for j in reversed(range(p, i + 1)):
                a = str(i * j)
                if a == a[::-1]:
                    if result < i * j:
                        result = i * j
        return result

    return -1


if __name__ == "__main__":
    print(solver(3, 100, 200))
    print(answer())
