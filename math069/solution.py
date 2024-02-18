"""
Totient Maximum
"""
def is_prime(num):
    """
    to chcek if a num is prime
    """
    for i in range(2, num):
        if num % i != 0:
            return False
    return True



def gcd(a, b):
    """
    This function finds the greatest common divisor (gcd).
    """
    while b:
        a, b = b, a % b
    return a


def euler_totient(n):
    """
    Euler's Totient Function to count numbers relatively prime to n.
    """
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


def answer(limit):
    """
    Find the value of n<=1000000
    for which n/phi(n)
    is a maximum.
    """
    max_totient = 0
    max_i = 0
    for i in range(2, limit):
        if not is_prime(i):
            totient = i / euler_totient(i)
            if totient > max_totient:
                max_totient = totient
                max_i = i

    return max_i


if __name__ == "__main__":
    print(answer(1000000))
