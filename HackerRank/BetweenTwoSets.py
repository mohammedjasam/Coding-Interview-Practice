# Consider two sets of positive integers, A and B. We say that a positive integer, X,
# is between sets A and B if the following conditions are satisfied:
#
# All elements in A are factors of X.
# X is a factor of all elements in B.
#
# A = {2,6}, B = {12}, Therefore, X = {6, 12}

n, m = map(int, input().split())
n = list(map(int,input().split()))
m = list(map(int,input().split()))

fac = []
ele = 0
for i in range(2, m[-1]):
    count = 0
    for j in n:
        if i % j == 0:
            count += 1

    if count == 2:
        fac.append(i)
# print(fac)

count = 0

for i in range(len(fac)):
    for x in m:
        for ele in fac:
            if x % ele == 0:
                a=1
            else:
                fac.remove(ele)
                # print(fac)

print(len(fac))
