print("Enter the number")

n = input()

s = n.split('0')

s.remove("")
for x in range(len(s)):
    if x == "":
        del s[x]
print(s)
