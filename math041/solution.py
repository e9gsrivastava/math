"""Pandigital Prime"""


def is_prime(n):
    """to find the prime number"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_permutations(digits):
        """all permutations of a number"""
        digits = list(str(digits))

        if len(digits) == 1:
            return digits
        all_perms = []
        for d in digits:
            removed = list(set(digits) - set([d]))
            perms = [d + rmn for rmn in all_permutations("".join(removed))]
            all_perms += perms
        return all_perms

def answer():
    for num in reversed(range(1,10)):
        digits=''.join(str(i) for i in range(1,num+1) )
        pan_d_list=all_permutations(int(digits))
        for i in sorted(pan_d_list)[::-1]:
            if is_prime(int(i)):
                    return i

if __name__ == "__main__":
    print(answer())





