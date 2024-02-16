
def same_digits(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

def answer():
    num = 1

    while True:
        if all(same_digits(num, num * i) for i in range(2, 7)):
            return num
        num += 1


print(answer())
