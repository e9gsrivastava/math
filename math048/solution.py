"""Self Powers"""


def answer():
    """Find the last ten digits of the series"""
    total_sum = 0
    for i in range(1, 1000):
        total_sum += i**i

    return str(total_sum)[-10:]


if __name__ == "__main__":
    print(answer())
