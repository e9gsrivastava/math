"""
Permuted Multiples
"""

def same_digits(n1, n2):
    """
    to chcek if two nums have same digits
    """
    return sorted(str(n1)) == sorted(str(n2))


def answer():
    """
    Find the smallest positive integer, x
    such that 2x,3x,4x,5x,6x contain the same digits.
    """
    num = 1

    while True:
        if all(same_digits(num, num * i) for i in range(2, 7)):
            return num
        num += 1


if __name__ == "__main__":
    print(answer())
