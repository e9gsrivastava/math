"""Consecutive Prime Sum"""


def is_prime(num):
    """this finds all the prime number"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def answer():
    """this finds the prime, below one-million,
    can be written as the sum of the most consecutive primes"""
    prime_numbers = []
    for num in range(1, 1000000):
        if is_prime(num):
            prime_numbers.append(num)

    max_length = 0
    result_sum = 0

    for start_index in range(len(prime_numbers)):
        for end_index in range(start_index + max_length, len(prime_numbers)):
            current_sum = sum(prime_numbers[start_index:end_index])
            if current_sum > 1000000:
                break
            if current_sum in prime_numbers:
                max_length = end_index - start_index
                result_sum = current_sum

    return result_sum


if __name__ == "__main__":
    print(answer())
