
def answer():
    p_list=[]
    for i in range(1000,3000):
        num=i*(3*i-1)/2
        p_list.append(int(num))
    for i in p_list:
        for j in p_list:
            if j-i in p_list and i+j in p_list:
                return (j-i)
            

print(answer())