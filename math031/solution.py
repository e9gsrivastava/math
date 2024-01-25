"""
Coin Sums
"""


def answer():
    """How many different ways can £2 be made using any number of coins?"""
    return solver(200)


coin_list = [1, 2, 5, 10, 20, 50, 100, 200]


def solver(target):
    """Generalize the solution in Part A to identify different ways to make any amount (£n)?"""
    combinations = [1] + [0] * target
    for coin in coin_list:
        for i in range(len(combinations) - coin):
            combinations[i + coin] += combinations[i]
    return str(combinations[-1])


if __name__ == "__main__":
    print(solver(100))
    print(answer())
