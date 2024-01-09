"""Name Scores"""


def answer():
    """score for names.txt"""

    return solver("0022_names.txt")


def solver(names: str):
    """names is the name of the file with all the names for processing"""

    with open(names, "r",encoding='utf-8') as f:
        reader = f.read()
        names = [
            i[1 : len(i) - 2] if "\n" in i else i[1 : len(i) - 1]
            for i in sorted(reader.split(","))
        ]

    names_score_dict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }

    score = 0
    for index, name in enumerate(names, 1):
        word = 0
        for letter in name:
            word += names_score_dict[letter]
        score += word * index
    return score


if __name__ == "__main__":
    print(solver("0022_names.txt"))
    print(answer())
