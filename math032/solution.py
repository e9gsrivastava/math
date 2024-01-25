"""
Pandigital Products
"""


def solver():
    '''We shall say that an -digit number is pandigital if it makes
    use of all the digits to exactly once'''
    
    d=['1','2','3','4','5','6','7','8','9']
    my_list=set()

    for i in range(10):
        for j in range(1000,10000):
            s=''
            s=s+str(i)
            s=s+str(j)
            s=s+str(i*j)
            if sorted(s) == d:
                my_list.add(i*j)

    for i in range(10, 100):
        for j in range(100,1000):
            s=''
            s=s+str(i)
            s=s+str(j)
            s=s+str(i*j)
            if sorted(s) == d:
                my_list.add(i*j)

    return sum(set(my_list))

if __name__=='__main__':
    print(solver())