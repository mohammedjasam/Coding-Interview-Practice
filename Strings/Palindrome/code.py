s = input()
r = "".join(x for x in list(reversed(s)))

if s == r:
    print("Yes")
else:
    print("No")

    
