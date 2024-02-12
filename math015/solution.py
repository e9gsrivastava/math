"""this is to find lattice path """


def solver(m: int, n: int):
    """this func sol for lattice path"""

    m = max(m, n)
    n = min(m, n)

    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        matrix[i][0] = 1

    for j in range(n + 1):
        matrix[j][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return sum(matrix[-1])


def answer():
    """this func sol for 20x20 grid lattice path"""

    return solver(20, 20)


if __name__ == "__main__":
    print(solver(20, 20))
    print(answer())
