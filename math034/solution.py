"""
Digit Factorials
"""


def solver():
    """Find the sum of all numbers which are equal to the
    sum of the factorial of their digits."""

    def fact(numbers):
        """it finds factorial of a num"""
        ans = 1
        for num in range(1, numbers + 1):
            ans *= num
        return ans

    result = []
    for i in range(3,1000000):
        fact_sum = 0
        for j in str(i):
            fact_sum += fact(int(j))
        if fact_sum == i:
            result.append(fact_sum)
    return sum(result)


if __name__ == "__main__":
    print(solver())
