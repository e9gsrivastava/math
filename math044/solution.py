"""Pentagon Numbers"""


def answer():
    """find pentagon number pk,pj for which their sum and difference
    is also pentagon number"""
    p_list = []
    for i in range(1000, 3000):
        num = i * (3 * i - 1) / 2
        p_list.append(int(num))
    for i in p_list:
        for j in p_list:
            if j - i in p_list and i + j in p_list:
                ans = j - i
                return ans
    return 0


if __name__ == "__main__":
    print(answer())
