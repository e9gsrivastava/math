def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True


prime_list=[]
for i in range(1,1000):
    if is_prime(i):
        prime_list.append(i)


s=0
c=0
for i in prime_list:
    # print(i)
    s+=i
    if s in prime_list:
        c=i
        r=s

print(c)
print(r)



# print(prime_list.index(3863))
# print(prime_list[536])