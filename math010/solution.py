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

    return solver(2,2000000)

if __name__ == "__main__":
    print(answer())
    print(solver(2,10))