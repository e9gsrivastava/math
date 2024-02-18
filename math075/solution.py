"""
Singular Integer Right Triangles
"""
def answer():
    """
    Given that L
    is the length of the wire, for how many values of L<=1500000
    can exactly one integer sided right angle triangle be formed?
    """
    limit=1500000
    count = 0
    perimeters = [0] * (limit + 1)

    for a in range(1, int((limit / 2) ** 0.5) + 1):
        for b in range(a, (limit - a) // 2 + 1):
            c_squared = a**2 + b**2
            c = int(c_squared**0.5)

            if c_squared == c**2 and a + b + c <= limit:
                perimeters[a + b + c] += 1

    count = sum(1 for p in perimeters if p == 1)
    return count

if __name__=="__main__":
    print(answer())
