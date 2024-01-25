"""
Digit Cancelling Fractions
"""


def solver():
    """There are exactly four non-trivial examples of this type of fraction,
      less than one in value, and containing
    two digits in the numerator and denominator.
    If the product of these four fractions is given in its lowest common terms,
      find the value of the denominator.
    """

    def special_div(num, den):
        """The special_div function is a helper function used in
          the solver function to find pairs of two-digit
            numbers num and den that satisfy certain conditions and
              return a simplified fraction.
            The conditions are:

        The tens digit of num is not equal to the tens digit of den.
        The tens digit of num is equal to the tens digit of den or the units
          digit of num is equal
          to the tens digit of den or the units digit of num is equal to the units
          digit of den.
        The tens digit of num and den are not in the ten_list (i.e.,
        [10, 20, 30, 40, 50, 60, 70, 80, 90]).
        The simplified fraction is not equal to 1."""

        ten_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        if str(num)[0] != str(num)[1] or str(den)[0] != str(den)[1]:
            if str(num)[0] == str(den)[0]:
                if (
                    int(str(den)[1]) != 0
                    and int(str(num)[1]) / int(str(den)[1]) == num / den
                    and num / den < 1
                    and num not in ten_list
                    and den not in ten_list
                ):
                    return int(str(num)[1]) / int(str(den)[1])

            if str(num)[0] == str(den)[1]:
                if (
                    int(str(den)[0]) != 0
                    and int(str(num)[1]) / int(str(den)[0]) == num / den
                    and num / den < 1
                    and num not in ten_list
                    and den not in ten_list
                ):
                    return int(str(num)[1]) / int(str(den)[0])

            if str(num)[1] == str(den)[0]:
                if (
                    int(str(den)[1]) != 0
                    and int(str(num)[0]) / int(str(den)[1]) == num / den
                    and num / den < 1
                    and num not in ten_list
                    and den not in ten_list
                ):
                    return int(str(num)[0]) / int(str(den)[1])

            if str(num)[1] == str(den)[1]:
                if (
                    int(str(den)[0]) != 0
                    and int(str(num)[0]) / int(str(den)[0]) == num / den
                    and num / den < 1
                    and num not in ten_list
                    and den not in ten_list
                ):
                    return int(str(num)[0]) / int(str(den)[0])
        return 0

    mylist = []
    for num in range(10, 100):
        for den in range(10, 100):
            if special_div(num, den) != 0:
                mylist.append(special_div(num, den))

    def gcd(num, den):
        """This function takes two arguments num and den and returns
        the greatest common divisor of num and den."""
        while den:
            num, den = den, num % den
        return num

    def decimal_to_fraction(decimal):
        """This function takes a decimal number decimal and returns
        a simplified fraction representation of decimal."""
        integer = int(decimal)
        decimal_part = abs(decimal - integer)

        denominator = 10 ** len(str(decimal_part)[2:])
        numerator = int(decimal_part * denominator)

        common_divisor = gcd(numerator, denominator)
        return denominator // common_divisor

    ans = 1
    for i in mylist:
        ans *= decimal_to_fraction(i)

    return ans


if __name__ == "__main__":
    print(solver())
