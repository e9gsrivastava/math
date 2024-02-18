"""
Spiral Primes
"""


def is_prime(num):
    """
    to check if a num is prime
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def answer():
    """
    If one complete new layer is wrapped around the
    spiral above, a square spiral with side length 9
    will be formed. If this process is continued, what is
    the side length of the square spiral for which the ratio
    of primes along both diagonals first falls below
    10%?
    """
    given_percent = 0.1
    primes_count = 0
    total_numbers = 1

    side_length = 1
    current_number = 1

    while True:
        side_length += 2

        for _ in range(4):
            corner = current_number + side_length - 1
            if is_prime(corner):
                primes_count += 1
            current_number = corner

        total_numbers += 4

        ratio = primes_count / total_numbers

        if ratio < given_percent:
            return side_length


if __name__ == "__main__":
    print(answer())
