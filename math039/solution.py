"""Integer Right Triangles"""


def count_right_angle_triangles(perimeter):
    """count the number of right angle traiangle"""
    count = 0
    for a in range(1, perimeter // 3):
        for b in range(a, (perimeter - a) // 2):
            c = perimeter - a - b
            if a**2 + b**2 == c**2:
                count += 1
    return count


def answer(limit):
    """For which value of limit=1000
    is the number of solutions maximised?"""
    max_triangles = 0
    result_perimeter = 0

    for p in range(1, limit):
        triangles_count = count_right_angle_triangles(p)
        if triangles_count > max_triangles:
            max_triangles = triangles_count
            result_perimeter = p
    return result_perimeter


if __name__ == "__main__":
    print(answer(1001))
