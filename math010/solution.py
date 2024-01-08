"""this is to find the sum of prime no"""


def solver(p:int, q=None):
    """this function performs above functionality"""

    def prime(n):
        """this function finds prime no"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if type(p) != int or (q is not None and type(q) != int):
        return None

    if q is None:
        num_range = range(2, p + 1)
    else:
        num_range = range(p, q + 1)

    x = [num for num in num_range if prime(num)]
    return sum(x)





def answer():
    """this is to find the sum of prime no"""

    def prime(n):
        """this function finds prime no"""
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = 2000000
    x = []
    i = 2
    while i < num:
        if prime(i) is True:
            x.append(i)
        i += 1
    return sum(x)


if __name__ == "__main__":
    print(answer())
    print(solver(2,10))