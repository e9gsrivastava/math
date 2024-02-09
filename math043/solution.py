prime_list=[2,3,5,7,11,13,17]
pandigital_list=['0','1','2','3','4','5','6','7','8','9']

pan_d_list=[]

def all_pan_num():
    return pan_d_list

result=[]
for i in pan_d_list:
    for j in range(8):
        num=str(i)[j+1:j+3]
        if int(num)%prime_list[j]!=0:
            break
    result.append(i)

print(result)
