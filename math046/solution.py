def odd_composite(num):
    if num%2==0:
        return False
    for i in range(3,num):
        if num%i==0:
            return True
    return False

def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

prime_list=[]
for i in range(10000):
    if is_prime(i):
        prime_list.append(i)

def answer():
    result=[]
    for i in range(1000):
        if odd_composite(i):
            for j in range(1,100):
                for k in range(1,1000):
                    if prime_list[k] +   2 * (j**2)==i:
                        return i,k,j
                
print(answer())