s = "JASAM"
r = ""
for x in range(len(s)-1,-1,-1):
    r += s[x]
print(r)


def rev(s):
    if len(s)<2:
        return s
    else:
        return rev(s[1:]) + s[0]
print(rev(s))
