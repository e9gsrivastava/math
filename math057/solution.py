"""
Square Root Convergents
"""
def answer():
    """
    In the first one-thousand expansions,
    how many fractions contain a numerator with more digits than the denominator?
    """
    num, den = 3, 2
    count = 0

    for _ in range(2, 1001):
        num, den = num + 2 * den, num + den
        if len(str(num)) > len(str(den)):
            count += 1

    return count


if __name__ == "__main__":
    print(answer())
