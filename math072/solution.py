"""
Counting Fractions
"""
def euler_totient(n):
    """
    Euler's Totient Function to count numbers relatively prime to n
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


def answer():
    """How many elements would be contained in
    the set of reduced proper fractions for d<=1000000
    """
    limit=1000000
    count = 0
    for d in range(2, limit + 1):
        count += euler_totient(d)

    return count

if __name__=="__main__":
    print(answer())
