"""Double-base Palindromes"""


def answer():
    """Find the sum of all numbers, less than one million, which are palindromic in base 10
    and base 2"""
    num = 585
    ans = []
    for i in range(1, 1000000):
        num = i
        if str(num) == str(num)[::-1]:
            remainder_list = []
            while num >= 1:
                remainder_list.append(num % 2)
                num = num // 2

            if remainder_list[::-1] == remainder_list:
                ans.append(i)

    return sum(ans)


if __name__ == "__main__":
    print(answer())
