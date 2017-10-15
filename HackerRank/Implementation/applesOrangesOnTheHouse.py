s, t = map(int,input().split())
a, b = map(int,input().split())
m, n = map(int,input().split())
m = map(int,input().split())
n = map(int,input().split())

mC = 0
for i in m:

    if s <= i + a <= t:
        mC +=1

nC = 0
for i in n:
    if s <= b + i <= t:
        nC +=1

print(mC,nC)
