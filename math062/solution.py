"""
Cubic Permutations
"""


def answer():
    """
    Find the smallest cube for which exactly five
    permutations of its digits are cube.
    """
    p = 5
    cubes_hash = {}
    n = 1
    while True:
        cube = n**3
        s = "".join(sorted(str(cube)))

        if s not in cubes_hash:
            cubes_hash[s] = [cube]
        else:
            cubes_hash[s].append(cube)

            if len(cubes_hash[s]) == p:
                return min(cubes_hash[s])

        n += 1


if __name__ == "__main__":
    print(answer())
