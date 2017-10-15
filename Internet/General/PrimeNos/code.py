size = int(input())

for i in range(size):
    count = 0
    for j in range(size, 0, -1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
