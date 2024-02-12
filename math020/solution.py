"""THIS IS TO FIND FACTORIAL N AND SUM OF ITS DIGITS"""


def solver(n):
    """THIS FUNC SOLVES ABOVE"""
    nums = [1]
    for i in range(1, n + 1):
        carry = 0
        for j, num in enumerate(nums):
            temp = num * i + carry
            nums[j] = temp % 10
            carry = temp // 10
        while carry > 0:
            nums.append(carry % 10)
            carry //= 10

    return sum(nums)


def answer():
    """THIS IS TO FIND FACTORIAL 100 AND SUM OF ITS DIGITS"""
    return solver(100)


if __name__ == "__main__":
    print(answer())
    print(solver(11))
