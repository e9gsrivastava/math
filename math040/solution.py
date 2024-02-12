"""Champernowne's Constant"""


def answer():
    """An irrational decimal fraction is created by concatenating the positive integers:"""

    num = 1000000
    i = 0
    irrational_str = ""
    while len(irrational_str) < num:
        i += 1
        irrational_str += "".join(str(i))

    ans = (
        int(irrational_str[1 - 1])
        * int(irrational_str[10 - 1])
        * int(irrational_str[100 - 1])
        * int(irrational_str[1000 - 1])
        * int(irrational_str[10000 - 1])
        * int(irrational_str[100000 - 1])
        * int(irrational_str[1000000 - 1])
    )
    return ans


if __name__ == "__main__":
    print(answer())
