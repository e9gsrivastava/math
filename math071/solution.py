# def decimal_smallest_fraction(num):
    

# def gcd(a, b):
#     """
#     this func finds the gcd
#     """
#     while b:
#         a, b = b, a % b
#     return a

# result=[]
# for i in range(1,100):
#     for j in range(i,1000000-1):
#         if gcd(i,j)==1:
#             result.append(f"{i} / {j}")

# print(result.index('3 / 7'))
# print(sorted(result)[12])
def find_fraction(limit):
    limit=1000000
    target_fraction = 3 / 7
    closest_numerator = 0
    closest_denominator = 1

    for denominator in range(1, limit + 1):
        numerator = denominator * target_fraction //1
        if numerator / denominator < target_fraction and numerator / denominator > closest_numerator / closest_denominator:
            closest_numerator = numerator
            closest_denominator = denominator

    return closest_numerator

print(find_fraction(1000000))

print(3/2//1)