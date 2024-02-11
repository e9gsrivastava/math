"""Prime Permutations"""


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def answer():
    """What 12-digit number do you form by
    concatenating the three terms in this sequence?"""
    for i in range(1488, 10000):
        x = i + 3330
        y = x + 3330
        if is_prime(i) and is_prime(x) and is_prime(y):
            if sorted(str(i)) == sorted(str(x)) == sorted(str(y)):
                return str(i) + str(x) + str(y)
    return -1


if __name__ == "__main__":
    print(answer())
