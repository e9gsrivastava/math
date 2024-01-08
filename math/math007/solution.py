"""this is find the nth prime no"""

def answer():
    """this func performs above func"""
    a = 10001

    def prime(n):
        """this func finds prime no"""

        if n < 2:
            return False
        for i in range(2, int(n ** (1 / 2) + 1)):
            if n % i == 0:
                return False
        return True

    x = []
    n = 2
    while a > len(x):
        if prime(n):
            x.append(n)

        n += 1
    return x[-1]


def solver(n: int):
    """this func finds nth pirme func"""

    def prime(num):
        """this func finds prime no"""
        if num < 2:
            return False
        for i in range(2, int(num ** (1 / 2) + 1)):
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


if __name__ == "__main__":
    print(solver(100001))
    print(answer())