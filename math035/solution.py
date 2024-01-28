"""
Circular Primes
"""


def answer():
    """How many circular primes are there below one million?"""
    return solver(1, 1000000)


def solver(p, q):
    """How many circular primes are there fromp to q ?"""

    def find_prime(n):
        """find the prime number"""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_circular_rotations(num):
        """find the circular roatations of a num"""

        str_num = str(num)
        circular_rotation_list = [
            int(str_num[i:] + str_num[:i]) for i in range(len(str_num))
        ]
        return circular_rotation_list

    ans = set()
    for i in range(p, q):
        if find_prime(i):
            x = find_circular_rotations(i)
            result = all(find_prime(j) for j in x)
            if result:
                ans.add(i)
    return len(list(ans))


if __name__ == "__main__":
    print(solver(1, 100))
    print(answer())
