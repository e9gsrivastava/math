def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True
pandigital_list=[['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8'],['1','2','3','4','5','6','7'],['1','2','3','4','5','6'],
                ['1','2','3','4','5'],['1','2','3','4'],['1','2','3'],['1','2']]


def is_pandigital(num):
    num=str(num)
    if sorted(num) in pandigital_list:
        return True
    return False

def answer():
    result=0
    for number in range(11,10000000):
        
        if is_prime(number) and is_pandigital(number) and number>c:
            result=number 
    return result


if __name__=='_main__':
    print(answer())