a = [1,2,2,3,3,3,4,4,4,5,6,6,9,8,6,6,5,4,5]

b = set(a)
count = 0
for x in b:    
    if a.count(x) == 1:
        print(x)
