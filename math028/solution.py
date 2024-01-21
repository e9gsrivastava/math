"""
Number Spiral Diagonals
"""


def answer():
    """What is the sum of the numbers on the diagonals in a 1001
    by 1001 spiral formed in the same way"""
    return solver(1001)


def solver(size):
    """What is the sum of the numbers on the diagonals in a n
    by n spiral formed in the same way"""
    if size % 2 == 0:
        return "enter odd num"

    diagonal_sum = 1
    current_value = 1
    for i in range(3, size + 1, 2):
        for _ in range(4):
            current_value += i - 1
            diagonal_sum += current_value

    return diagonal_sum


if __name__ == "__main__":
    print(solver(4))
    print(answer())
