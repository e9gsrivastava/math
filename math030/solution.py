"""
Digit Fifth Powers
"""


def answer():
    '''Find the sum of all the numbers that can be written
    as the sum of fifth powers of their digits.'''
    return solver(5)


def solver(n):
    '''Can you generalize the solution in Part A to find the sum of all
    the numbers that can be written as the sum of the nth powers of their digits?'''
    final_sum =0
    for i in range(2, 10000000):
        current_sum = 0
        for j in range(len(str(i))):
            current_sum += int(str(i)[j]) ** n
        if current_sum == i:
            final_sum+=i
    return final_sum


if __name__ == "__main__":
    print(answer())
    print(solver(4))
