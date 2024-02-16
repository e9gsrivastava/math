def factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i

    return result

def answer():
    for n in range(100):
        c=0
        for r in range(100):
            ans=factorial(n)/(factorial(n-r)*factorial(r))
            if ans>1000000:
                c+=1
    return c
if __name__=="__main__":
    print(answer())