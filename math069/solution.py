
def gcd(a, b):
    """
    this func finds the gcd
    """
    while b:
        a, b = b, a % b
    return a

def number_relative_prime(num):
    """
    this func finds the number of relative primes
    """
    c=1
    for i in range(2,num):
        if gcd(num,i)==1:
            c+=1
    return c
def is_prime(num):
    for i in range(2,num):
        if num%i!=0:
            return False
    return True

def answer():
    max_totient=0
    for i in range(1000000):
        if not is_prime(i): 
            c=i/number_relative_prime(i)
            if c>max_totient:
                max_totient=max(c,max_totient)

    return max_totient

if __name__=="__main__":
    print(answer())