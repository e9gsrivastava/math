"""Pandigital Multiples"""

def answer():
    """What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer """
    result = 0
    for i in range(1, 10000):
        concatenated_product = ""
        n = 1
        while len(concatenated_product) <9:
            concatenated_product += str(i * n)
            n += 1
        if sorted(concatenated_product)==["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            result = max(result, int(concatenated_product))
    return result

if __name__ == "__main__":
    print(answer())
