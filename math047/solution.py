"""Distinct Primes Factors"""


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def distinct_prime_factors_count(num, prime_list):
    """Count the number of distinct prime factors for a given number."""
    count = 0
    for prime in prime_list:
        if prime > num:
            break
        if num % prime == 0:
            count += 1
            while num % prime == 0:
                num //= prime
    return count


def find_consecutive_numbers():
    """Find the first four consecutive integers to have four distinct prime factors each.
    What is the first of these numbers?"""
    prime_list = [i for i in range(10000) if is_prime(i)]

    for i in range(100000, 150000):
        if all(distinct_prime_factors_count(i + j, prime_list) == 4 for j in range(4)):
            return i
    return 0


if __name__ == "__main__":
    print(find_consecutive_numbers())
