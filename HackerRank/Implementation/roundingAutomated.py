n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
print(l)
for x in l:
    if x >=38:
        if (x % 5) > 2 :
            print(x + (5 - (x % 5)))
        else:
            print(x)
    else:
        print(x)
