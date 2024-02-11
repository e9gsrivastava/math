'''Goldbach's Other Conjecture'''
def odd_composite(num):
    """to find odd composite"""
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return True
    return False


def is_prime(num):
    """to check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def answer():
    """What is the smallest odd composite that cannot
    be written as the sum of a prime and twice a square?"""
    prime_list = [i for i in range(10000) if is_prime(i)]
    for odd_comp in range(35, 100000, 2):
        if not odd_composite(odd_comp):
            continue
        found = False
        for prime in prime_list:
            if prime > odd_comp:
                break
            for j in range(1, 100):
                if prime + 2 * (j**2) == odd_comp:
                    found = True
                    break
            if found:
                break
        if not found:
            return odd_comp


if __name__ == "__main__":
    print(answer())
