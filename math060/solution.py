# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def check_concatenated_primes(p_list, num):
#     for i in p_list:
#         if not (is_prime(int(str(i) + str(num))) and is_prime(int(str(num) + str(i)))):
#             return False
#     return True

# def answer():
#     result = []
#     prime_list = []

#     num = 2
#     while len(result) < 5:
#         if is_prime(num):
#             prime_list.append(num)
#             if check_concatenated_primes(prime_list, num):
#                 result.append(num)
#         num += 1

#     return sum(result)

# print(answer())
