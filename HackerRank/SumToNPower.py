# Find the number of ways that a given integer, , can be expressed as the sum of the  power of unique, natural numbers.
# Sample Input
# 10
# 2
# Sample Output
# 1
# Since, 10 = 1^2 + 3^2


def findPowerSum( total,  power,  num):
    value = total - pow(num, power)
    if(value < 0):
         return 0
    elif(value == 0):
         return 1
    else:
        return findPowerSum(value , power, num + 1) + findPowerSum(total, power, num+1)

total = int(input())
power = int(input())
print(findPowerSum(total, power, 1))
