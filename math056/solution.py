def find_digits_sum(num):
    """
    find the sum of digits of a num
    """
    digits_list=sorted(str(num))
    digits_sum=0
    for i in digits_list:
        digits_sum+=int(i)
    
    return digits_sum


def answer():
    result=0
    for a in range(1,101):
        for b in range(1,101):
            result+=find_digits_sum(a**b)

    return result

if __name__=="__main__":
    print(answer())