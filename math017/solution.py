"""Number Letter Counts"""


def solver(a, b):
    """generalised sol for answer"""

    hash_dict = {
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
        # pylint: disable=R0912
        """numbers to words"""
        ans = ""
        if num == 0:
            ans = ""
        elif num < 0:
            ans = "enter positive num"

        elif num <= 20:
            ans = hash_dict[num]

        elif num < 100:
            if num % 10 != 0:
                ans = hash_dict[num // 10 * 10] + hash_dict[num % 10]
            else:
                ans = hash_dict[num // 10 * 10]

        elif num < 1000:
            hundreds = number_to_words(num // 100) + hash_dict[100]
            rest = number_to_words(num % 100)
            if rest and num % 100 != 0:
                ans = hundreds + "and" + rest
            else:
                ans = hundreds + rest

        elif num < 1000000:
            thousands = number_to_words(num // 1000) + hash_dict[1000]
            rest = number_to_words(num % 1000)
            if rest and num % 1000 != 0:
                ans = thousands + "and" + rest
            else:
                ans = thousands + rest

        elif num < 1000000000:
            millions = number_to_words(num // 1000000) + hash_dict[1000000]
            rest = number_to_words(num % 1000000)
            if rest:
                ans = millions + rest
            else:
                return millions
        else:
            ans = "enter range less than 1 billion"
        return ans

    total_letters = [len(number_to_words(i)) for i in range(a, b + 1)]
    return sum(total_letters)


def answer():
    """If all the numbers from 1 to 1000(one thousand) inclusive
    were written out in words, how many letters would be used?"""
    return solver(1, 1000)


if __name__ == "__main__":
    print(solver(1, 2))
    print(answer())
