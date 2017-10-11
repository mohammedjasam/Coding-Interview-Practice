# def prime_factors(n):
#     factors = []
#     d = 2
#     while (d * d <= n):
#         while ( n > 1 ):
#             while n % d == 0:
#                 factors.append(d)
#                 n = n / d
#             d += 1
#     print(factors)
#
# prime_factors(int(input()))
#
#
#
#
# def s(a):
#     if a // 10 == 0:
#         return a
#     return s(a//10) + s(a%10)
# n = 1234
# print(s(n))
def is_power2(num):

	'states if a number is a power of two'

	return num != 0 and ((num & (num - 1)) == 0)

print(is_power2(7))
