"""Pandigital Multiples"""


def find_largest_pandigital_product():
    """
    Finds the largest pandigital concatenated product of a number and its factors.

    Returns:
    int: The largest pandigital concatenated product.

    This function iterates through base numbers up to 10,000 and checks
      for pandigital concatenated products
    by multiplying each base number by integers from 1 to 9. The result is
      the largest pandigital concatenated product found.
    """
    pandigital_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    concatenated_products = []

    for base_number in range(1, 10):
        current_digits = []
        for multiplier in range(1, 10):
            current_digits.append(str(base_number * multiplier))
            if sorted(current_digits) == pandigital_digits:
                concatenated_products.append(current_digits)
                break
        print(current_digits)

    concatenated_as_integers = [
        int("".join(digits)) for digits in concatenated_products
    ]

    return sorted(concatenated_as_integers)[-1]


if __name__ == "__main__":
    print(find_largest_pandigital_product())
