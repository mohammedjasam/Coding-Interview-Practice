s = input()
li = []

d = {}
for x in range(len(s)):
    a = s[x]
    if a in d:
        d[s[x]].append(x)
    else:
        d[s[x]] = [x]

print(d)
mini = 0
for k, v in d.items():
    if len(v) == 1:
        print(k)
        break    
