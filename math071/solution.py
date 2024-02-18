"""
Ordered Fractions
"""
def answer():
    """
    By listing the set of reduced proper fractions for d<=1000000
    in ascending order of size, find the numerator of the fraction immediately to the left of 3/7
    """
    limit = 1000000
    target_fraction = 3 / 7
    closest_numerator = 0
    closest_denominator = 1

    for denominator in range(1, limit + 1):
        numerator = denominator * target_fraction // 1
        if (
            numerator / denominator < target_fraction
            and numerator / denominator > closest_numerator / closest_denominator
        ):
            closest_numerator = numerator
            closest_denominator = denominator

    return closest_numerator

if __name__=="__main__":
    print(answer())
