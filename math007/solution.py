"""this is find the nth prime no"""


def solver(n: int):
    """this func finds nth pirme func"""

    def prime(num):
        """this func finds prime no"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5 + 1)):
            if num % i == 0:
                return False
        return True

    x = []
    num = 2
    while n > len(x):
        if prime(num):
            x.append(num)

        num += 1
    return x[-1]


def answer():
    """this func performs above func"""
    return solver(10001)


if __name__ == "__main__":
    print(solver(1001))
    print(answer())
