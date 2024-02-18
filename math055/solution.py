"""
Lychrel Numbers
"""


def is_palindrome(num):
    """
    to check if a num is palindrome
    """
    return str(num) == str(num)[::-1]


def lychrel(num, max_iterations=50):
    """
    to check if a num is lychrel
    """
    for _ in range(max_iterations):
        num = num + int(str(num)[::-1])
        if is_palindrome(num):
            return False
    return True


def answer():
    """
    How many Lychrel numbers are there below ten-thousand?
    """
    count = 0
    for num in range(10000):
        if lychrel(num):
            count += 1
    return count


if __name__ == "__main__":
    print(answer())
