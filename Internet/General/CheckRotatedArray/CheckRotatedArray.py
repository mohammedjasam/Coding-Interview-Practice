from collections import deque

print("Enter the size of Array")
sizeA = int(input())
arrayA = []
for i in range(sizeA):
    arrayA.append(int(input()))

print("Enter the size of Array")
sizeB = int(input())
arrayB = []
for i in range(sizeB):
    arrayB.append(int(input()))

if sizeA != sizeB:
    print("No")

if set(arrayA).difference(arrayB):
    print("No")

arrayA, arrayB = deque(arrayA), deque(arrayB)

ans = False
for i in range(sizeA):
    arrayA.rotate()
    print(arrayA)
    if arrayA == arrayB:
       ans = True

if ans == True:
    print("yes")
