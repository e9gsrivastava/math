answer=[]
pan_digital=['1', '2', '3', '4', '5', '6', '7', '8', '9']
prod=[]
ss=[]

for i in range(1,10000):
    my_list=[]
    for j in range(1,10):
        my_list.extend(str(i*j))
        if sorted(my_list)==pan_digital:
            answer.append(i)
            prod.append(j)
            ss.append(my_list)
            break
        
print(answer)
result={answer[i]:prod[i] for i in range(len(answer))}
print(result)
print(ss)
l=[]
for i in ss:
    k=''
    k=''.join(i)
    l.append(int(k))

print(sorted(l)[-1])