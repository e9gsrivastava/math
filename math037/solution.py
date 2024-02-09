def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def answer():
    ans=[]
    for i in range(10,1000000):
        my_list=[]
        if is_prime(i):
            i=str(i)
            for j in range(1,len(i)):
                numl=i[j:]
                numr=i[:-j]
                my_list.append(is_prime(int(numl)))
                my_list.append(is_prime(int(numr)))
            if False in my_list:
                pass
            else:
                ans.append(int(i))   

    return sum(ans)


if __name__=='__main__':
    print(answer())