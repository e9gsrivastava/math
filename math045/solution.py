t_list=[]
p_list=[]
h_list=[]
for i in range(1,10000):
    t_list.append(i*(i+1)/2)
    p_list.append(i*(3*i-1)/2)
    h_list.append(i*(2*i-1))

for i in t_list[285:]:
    if i in p_list and h_list:
        print(i)
        break