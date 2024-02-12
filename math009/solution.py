"""this is to calacualte pythagorean triplet whose sum is 1000"""


def answer():
    """this function does above task"""
    for i in range(1, 1000):
        for j in range(i, 1000):
            k = 1000 - i - j
            if i**2 + j**2 == k**2:
                x = i * j * k
                return x


def solver(p, q=None):
    """calacualte pythagorean triplet"""
    my_dict = {}
    if q is None:
        q = p
    for i in range(1, q + 1):
        for j in range(i, q + 1):
            k = (i**2 + j**2) ** 0.5
            if k == int(k):
                k = int(k)
                triplet = tuple(sorted([i, j, k]))

                if p <= sum(triplet) <= q:
                    s = sum(triplet)
                    if s not in my_dict:
                        my_dict[s] = [triplet]
                    else:
                        my_dict[s].append(triplet)

    return my_dict


if __name__ == "__main__":
    print(solver(2, 100))
    print(answer())
