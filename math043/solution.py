"""Sub-string Divisibility"""
def answer():
    """Find the sum of all 0 to 9 pandigital
    numbers with this property."""
    prime_list = [2, 3, 5, 7, 11, 13, 17]

    def all_permutations(digits):
        """all permutations of a number"""
        digits = list(str(digits))

        if len(digits) == 1:
            return digits
        all_perms = []
        for d in digits:
            removed = list(set(digits) - set([d]))
            perms = [d + rmn for rmn in all_permutations("".join(removed))]
            all_perms += perms
        result = []
        for i in all_perms:
            if i[0] != "0":
                result.append(i)
        return result

    pan_d_list = all_permutations(1234567890)
    result = []
    for i in pan_d_list:
        for j in range(7):
            num = str(i)[j + 1 : j + 4]
            if int(num) % prime_list[j] != 0:
                break
        result.append(int(i))
    return sum(result)

if __name__ == "__main__":
    print(answer())
