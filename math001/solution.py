"""answer func"""


def answer():
    """this finds facotrs"""
    x = []
    y = []
    for i in range(1000):
        if i % 3 == 0:
            x.append(i)
        if i % 5 == 0 and i not in x:
            y.append(i)

    return sum(x + y)


def solver(factors, start, end):
    """this finds facotrs"""
    total_sum = 0
    for i in range(start, end + 1):
        if any(i % fact == 0 for fact in factors):
            total_sum += i
    return total_sum


if __name__ == "__main__":
    print(solver([2, 3, 5, 7, 11], 34567, 1234567))
    print(answer())
