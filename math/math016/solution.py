"""this is to find 2**n where n is a very large no """
def solver(n):
    """this func does above task"""
    num = [2]
    if n==0:
        return 1
    for _ in range(n - 1):
        remainder = 0
        for i in reversed(range(len(num))):
            temp = num[i] * 2 + remainder
            num[i], remainder = temp % 10, temp // 10
            if remainder > 0 and i == 0:
                num.insert(0, remainder)
    return sum(num)


def answer():
    """this func calls generic func to get the value of 2**100"""

    return solver(1000)





if __name__ == "__main__":
    print(solver(1000))
    print(answer())