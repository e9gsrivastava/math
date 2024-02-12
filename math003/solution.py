"""this is to find prime number"""


def answer(c):
    """the largest prime factor of the number 600,851,475,143?"""

    k = int(c ** (0.5))
    l = []
    for i in range(1, k + 1):
        if c % i == 0:
            l.append(i)

    result = [int(c / i) for i in l]
    l.extend(result)

    prim = []
    for j in l:
        for i in range(2, j):
            if j % i == 0:
                break
        else:
            prim.append(j)

    return max(prim)


def solver(value):
    """the largest prime factor of the number"""
    k = int(value ** (0.5))

    l = []
    for i in range(1, k + 1):
        if value % i == 0:
            l.append(i)

    result = [int(value / i) for i in l]

    l.extend(result)
    prim = []
    for j in l:
        for i in range(2, j):
            if j % i == 0:
                break
        else:
            prim.append(j)

    return max(prim)


if __name__ == "__main__":
    print(solver(529))
    print(answer(600851475143))
