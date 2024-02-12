"""convert num to its spelling"""


def solver(a, b):
    """all the numbers from a to b
    (one thousand) inclusive were written out in words,
    how many letters would be used"""

    hash_dict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand",
        1000000: "million",
        1000000000: "billion",
    }

    def number_to_words(num):
        """Converts a number into English spelling"""
        if num < 0:
            return "enter postive num "

        if num <= 20:
            return hash_dict[num]

        if num < 100:
            if num % 10 != 0:
                return hash_dict[num // 10 * 10] + hash_dict[num % 10]

            return hash_dict[num // 10 * 10]

        if num < 1000:
            hundreds = number_to_words(num // 100) + hash_dict[100]
            rest = number_to_words(num % 100)
            if rest:
                return hundreds + rest

            return hundreds

        if num < 1000000:
            thousands = number_to_words(num // 1000) + hash_dict[1000]
            rest = number_to_words(num % 1000)
            if rest:
                return thousands + rest

            return thousands

        if num < 1000000000:
            millions = number_to_words(num // 1000000) + hash_dict[1000000]
            rest = number_to_words(num % 1000000)
            if rest:
                return millions + rest

            return millions

        return "enter range less than 1 billion "

    total_letters = [len(number_to_words(i)) for i in range(a, b + 1)]
    return sum(total_letters)


def answer():
    """all the numbers from 1 to 1000
    (one thousand) inclusive were written out in words,
    how many letters would be used"""

    return solver(1, 1000)


if __name__ == "__main__":
    print(solver(1, 2))
    print(answer())
