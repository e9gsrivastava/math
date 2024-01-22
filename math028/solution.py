"""
Number Spiral Diagonals
"""


def answer():
    """What is the sum of the numbers on the diagonals in a 1001
    by 1001 spiral formed in the same way"""
    return solver(1001)


def solver(n):
    """What is the sum of the numbers on the diagonals in a n
    by n spiral formed in the same way"""

    if n == 0:
        return 0

    current_value, diagonal_sum, total_sum = 1, 0, 0

    if n % 2 != 0:
        current_value, diagonal_sum, total_sum = 2, 1, 1

    for layer in range(current_value, n, 2):
        for _ in range(4):
            diagonal_sum += layer
            total_sum += diagonal_sum

    return total_sum


if __name__ == "__main__":
    print(solver(4))
    print(answer())
