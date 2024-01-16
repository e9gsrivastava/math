"""
Reciprocal Cycles
"""


def answer():
    """Find the value of d<1000 for which 1/d contains the longest recurring cycle
    in its decimal fraction part."""
    return solver(1000)


def solver(num, digits=None):
    """Generalize the solution in Part A to find the value of for which
    contains all the digits in the provided
    list in the recurring cycle in its decimal fraction part."""

    my_list = []
    longest = 0
    for i in range(2, num + 1):
        remainder_set = []
        dividend = 1 // i
        c_length = 0
        remainder = 1
        recurring_cycle = ""

        while remainder not in remainder_set and remainder != 0:
            remainder_set.append(remainder)

            dividend = (remainder * 10) // i
            remainder = (remainder * 10) % i
            c_length += 1
            recurring_cycle += str(dividend)

        if remainder == 0:
            my_list.append(recurring_cycle)
        else:
            temp = remainder_set.index(remainder)
            my_list.append(recurring_cycle[temp:])
        if longest < c_length:
            longest = c_length
            ans = i

    if not digits:
        return ans

    for index, i in enumerate(my_list, 2):
        if digits[0] == i:
            return index
        return 0


if __name__ == "__main__":
    print(answer())
    print(solver(1001, ["001"]))
