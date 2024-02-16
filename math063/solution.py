def answer():
    c = 0
    for i in range(1, 10):
        j = 1
        while len(str(i**j)) == j:
            c += 1
            j += 1

print(answer())
