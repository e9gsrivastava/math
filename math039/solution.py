# ans=set()
# for i in range(1,1000):
#     for j in range(1,1000):
#         z=(i**2 + j**2)**0.5
#         if z**0.5 == int(z**0.5) and i+j+z<1000:
#             ans.add((i,j,int(z)))
# print(ans)
# d={}
# for i in ans:
#     # print(i)
#     if sum(i) in d:
#         d[sum(i)].append(i)
#     else:
#         d[sum(i)]=[i]
# print(sorted(d))










ans=set()
for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):

        
            if k**2 == i**2+j**2 and i+j+k<1000:
                ans.add((i,j,k))
print(ans)
d={}
for i in ans:
    # print(i)
    if sum(i) in d:
        d[sum(i)].append(i)
    else:
        d[sum(i)]=[i]
print((d))