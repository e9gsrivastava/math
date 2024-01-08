'''this function finds the What is the value of the
first triangle number to have over five hundred divisors?'''


def solver(req_divisors):
    """this func does above task"""

    def find_factors(num):
        """this func finds the no of factors of a given no"""
        count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                count += 2

        # check for no is perfect sq.
        if int(num**0.5) ** 2 == num:
            count = count - 1
        return count

    t_sum = 1
    i = 2
    while True:
        t_sum += i
        i += 1
        if find_factors(t_sum) > req_divisors:
            return t_sum






def answer():
    """first triangle number to have over five hundred divisors?"""
    req_divisors = 500

    def find_factors(num):
        """this func finds the no of factors of a given no"""
        count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                count += 2
        if int(num**0.5) ** 2 == num:
            count = count - 1
        return count

    t_sum = 1
    i = 2
    while True:
        t_sum += i
        i += 1
        if find_factors(t_sum) > req_divisors:
            return t_sum



if __name__ == "__main__":
    print(solver(16))
    print(answer())
