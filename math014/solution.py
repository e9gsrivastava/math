"""he number which returns the longest collatz sequence such that the number is between 
(a) 1 and p if only p is defined and (b) p and q if both p and q are defined"""


def collatz(n, hash_dict):
    """this finds one less than collatz no's length"""

    my_list = []
    while n != 1:
        my_list.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n in hash_dict:
            return hash_dict[n] + len(my_list)
    return len(my_list)


def solver(p: int = None, q: int = None):
    """performs above task"""
    hash_dict = {}
    if p is None and q is None:
        return None
    if p is not None and q is None:
        q = p
        p = 2

    resultant_num = 0
    max_length = 0

    for i in range(2, q):
        current_length = collatz(i, hash_dict)
        if current_length > max_length:
            max_length = current_length
            resultant_num = i
        hash_dict[i] = current_length
    return resultant_num


def answer():
    """this finds Which starting number, under one million, produces the longest collatz chain?"""

    return solver(1000000)


if __name__ == "__main__":
    print(solver(2, 1000000))
    print(answer())
