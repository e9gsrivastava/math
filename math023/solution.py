"""Non-Abundant Sums"""


def answer():
    """this function finds Find the sum of all the positive integers which
    cannot be written as the sum of two abundant numbers."""

    return solver(28123)


def solver(n):
    """this function finds Find the sum of all the positive integers which
    cannot be written as the sum of two abundant numbers."""
    abundant_list = []

    for i in range(1, n + 1):
        temp = 0
        for j in range(1, int(i)):
            if i % j == 0:
                temp += j

        if temp > i:
            abundant_list.append(i)

    sum_abundant_num = [
        abundant_list[i] + abundant_list[j]
        for i in range(len(abundant_list))
        for j in range(i, len(abundant_list))
    ]

    all_num = set(range(1, 28124))
    result = all_num - set(sum_abundant_num)

    return sum(result)


if __name__ == "__main__":
    print(answer())
    print(solver(123))
