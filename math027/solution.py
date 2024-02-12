"""
Quadratic Primes
"""


def answer():
    """Find the product of the coefficients,a and b,
    for the quadratic expression that produces the maximum number of
      primes for consecutive values of n, starting with n=0."""

    def is_prime(n):
        """func to find prime num"""
        if n <= 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    hash_dict = {}
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            num = 0

            while is_prime(num**2 + a * num + b):
                num += 1
            hash_dict.update({num: a * b})
    key = sorted(hash_dict, reverse=True)[0]
    return hash_dict[key]


if __name__ == "__main__":
    print(answer())
