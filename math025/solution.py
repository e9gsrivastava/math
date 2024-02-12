"""
1000-digit Fibonacci
"""


def answer():
    """What is the index of the first term in the Fibonacci sequence to contain
    1000 digits?"""
    return solver(1000)


def solver(length: int):
    """Generalize the solution in Part A to identify
    the first term in the Fibonacci sequence to contain ndigits."""

    def add_large_digits(num1, num2):
        """func to add two nums unit digitwise"""
        num1, num2 = str(num1), str(num2)
        result = []
        carry = 0

        diff = len(num1) - len(num2)
        if diff > 0:
            num2 = "0" * diff + num2
        elif diff < 0:
            num1 = "0" * abs(diff) + num1

        for i in range(len(num1) - 1, -1, -1):
            digit1 = int(num1[i])
            digit2 = int(num2[i])

            total = digit1 + digit2 + carry
            result_digit = total % 10
            carry = total // 10

            result.insert(0, str(result_digit))

        if carry > 0:
            result.insert(0, str(carry))

        final = "".join(result)
        return int(final)

    def fibonacci(length):
        """func to find fibonacci series"""
        x, y = 1, 1
        index = 2
        while True:
            x, y = y, add_large_digits(x, y)
            index += 1

            if len(str(y)) == length:
                return index

    return fibonacci(length)


if __name__ == "__main__":
    print(answer())
    print(solver(2))
