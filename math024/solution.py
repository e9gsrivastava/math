"""
Lexicographic Permutations
"""


def answer():
    """what is Lexicographic Permutations of millionth
    for '0123456789'"""
    p = "0123456789"
    q = 1000000
    return solver(p, q)


def factorial(n):
    """func to find factorial"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def solver(elements: str, target):
    """identify the nth lexicographic permutation
    of a list of numbers and letters."""
    target = target - 1
    permutation = []
    left_elements = list(elements)

    for i in range(len(elements) - 1, -1, -1):
        index = target // factorial(i)
        target %= factorial(i)
        permutation.append(left_elements.pop(index))

    return "".join(permutation)


if __name__ == "__main__":
    print(answer())
    print(solver("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10000000000000))
