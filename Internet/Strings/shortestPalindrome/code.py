# s = input()
s = "abcd"

for i in range(len(s)):
    r = ""
    for j in range(i+1):
        r += s[j]
    r = "".join(x for x in list(reversed(r)))
    if s + r == "".join(x for x in list(reversed(s + r))):
        print(s+"".join(x for x in list(reversed(r))))
        break
