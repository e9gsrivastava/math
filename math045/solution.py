'''Triangular, Pentagonal, and Hexagonal'''
def answer():
    '''Find the next triangle number after 285 
    that is also pentagonal and hexagonal.'''
    t_list = []
    p_list = []
    h_list = []
    for i in range(1, 100000):
        t_list.append(i * (i + 1) / 2)
        p_list.append(i * (3 * i - 1) / 2)
        h_list.append(i * (2 * i - 1))

    for i in t_list[285:]:
        if i in p_list and i in h_list:
            return int(i)
        return 0

if __name__ == "__main__":
    print(answer())
