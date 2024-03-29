"""this finds maax sum in traingle problem"""


def solver(s: str):
    """By starting at the top of the triangle below and moving to
    adjacent numbers on the row below, the maximum total from top to bottom is 23"""

    lines = s.split("\n")
    two_d_list = [[int(num) for num in line.split()] for line in lines]
    for i in reversed(range(len(two_d_list) - 1)):
        for j in range(len(two_d_list[i])):
            two_d_list[i][j] += max(two_d_list[i + 1][j], two_d_list[i + 1][j + 1])

    max_total = two_d_list[0][0]

    return max_total


def answer():
    """By starting at the top of the triangle below and moving to
    adjacent numbers on the row below, the maximum total from top to bottom is 23"""

    triangle_str = """75
                    95 64
                    17 47 82
                    18 35 87 10
                    20 04 82 47 65
                    19 01 23 75 03 34
                    88 02 77 73 07 63 67
                    99 65 04 28 06 16 70 92
                    41 41 26 56 83 40 80 70 33
                    41 48 72 33 47 32 37 16 94 29
                    53 71 44 65 25 43 91 52 97 51 14
                    70 11 33 28 77 73 17 78 39 68 17 57
                    91 71 52 38 17 14 91 43 58 50 27 29 48
                    63 66 04 68 89 53 67 30 73 16 69 87 40 31
                    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 """

    return solver(triangle_str)


if __name__ == "__main__":
    TRIANGLE_STR = """3
                    7 4
                   2 4 6
                  8 5 9 3"""
    print(solver(TRIANGLE_STR))
    print(answer())
