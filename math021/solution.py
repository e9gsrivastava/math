"""module:solution.py
this assigment is about amicable number"""


def answer():
    """this func finds the amicabale numbers's sum under 10000"""

    return solver(1, 10000)


def amicable(num):
    """this function checks for amicable number"""
    num_fact = []

    for n in range(1, num):
        if num % n == 0:
            num_fact.append(n)

    sum_num_fact = sum(num_fact)

    fact_second = []

    if sum_num_fact != num:
        for k in range(1, sum_num_fact):
            if sum_num_fact % k == 0:
                fact_second.append(k)

        sum_fact_second = sum(fact_second)

        if sum_fact_second == num:
            return sum_fact_second + sum_num_fact
    return None


def solver(p: int, q: int):
    """this is to find the general amicable number"""

    start = min(p, q)
    end = max(p, q) + 1
    result = [amicable(num) for num in range(start, end) if amicable(num)]

    return sum(set(result))


if __name__ == "__main__":
    print(answer())
    print(solver(1, 1000))
