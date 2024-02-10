# ans=set()
# for i in range(1,1000):
#     for j in range(1,1000):
#         for k in range(1,1000):

        
#             if k**2 == i**2+j**2 and i+j+k<1000:
#                 ans.add((i,j,k))
# print(ans)
# d={}
# for i in ans:
#     # print(i)
#     if sum(i) in d:
#         d[sum(i)].append(i)
#     else:
#         d[sum(i)]=[i]
# print((d))



from collections import Counter

def find_most_common_perimeter(limit):
    counter = Counter()

    for i in range(1, limit // 2):
        for j in range(i, limit // 2):
            k = limit - i - j
            if k > 0 and k**2 == i**2 + j**2:
                counter[i + j + k] += 1

    most_common_perimeter, _ = counter.most_common(1)[0]
    return most_common_perimeter

if __name__ == "__main__":
    result = find_most_common_perimeter(1000)
    print(result)
