"""
Prime Pair Sets
"""


def is_prime(n):
    """to check if a num is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def answer():
    """
    Find the lowest sum for a set of five primes
    for which any two primes concatenate to produce another prime.
    """
    primes = [i for i in range(2, 10000) if is_prime(i)]

    for p1 in primes:
        for p2 in primes:
            if p2 > p1:
                if is_prime(int(str(p1) + str(p2))) and is_prime(
                    int(str(p2) + str(p1))
                ):
                    for p3 in primes:
                        if p3 > p2:
                            if all(
                                is_prime(int(str(p) + str(p3)))
                                and is_prime(int(str(p3) + str(p)))
                                for p in [p1, p2]
                            ):
                                for p4 in primes:
                                    if p4 > p3:
                                        if all(
                                            is_prime(int(str(p) + str(p4)))
                                            and is_prime(int(str(p4) + str(p)))
                                            for p in [p1, p2, p3]
                                        ):
                                            for p5 in primes:
                                                if p5 > p4:
                                                    if all(
                                                        is_prime(int(str(p) + str(p5)))
                                                        and is_prime(
                                                            int(str(p5) + str(p))
                                                        )
                                                        for p in [p1, p2, p3, p4]
                                                    ):
                                                        return sum([p1, p2, p3, p4, p5])
    return -1


if __name__ == "__main__":
    print(answer())
