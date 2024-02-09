
def answer():
    s=0
    for i in range(1,1000):
        s+=i**i

    print(str(s)[-10:])

if __name__=='__main__':
    print(answer())