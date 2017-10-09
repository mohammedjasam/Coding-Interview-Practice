from collections import deque

## THIS CODE PERMUTES!!!
def toString(List):
    return ''.join(List)
li = []
def permute(a, l, r): # starting and ending indices
    if l==r:
        li.append(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
    return li

## DATA
dist = {
        1:[(2,10),(3,15),(4,20)],
        2:[(1,10),(3,35),(4,25)],
        3:[(1,15),(2,35),(4,30)],
        4:[(1,20),(2,25),(3,30)]
        }



string = "1234" ## Four cities in the graph
n = len(string)
a = list(string)
li = permute(a, 0, n-1) # Permuted list

## Calculates the distance between 2 points A-B
def retDist(a, b):
    x = dict(dist[a])
    return x[b]

def sendPattern(n):
    summ = 0
    a, b = deque(n), deque(n)

    for i in range(len(n)-1):
        b.rotate()
    a, b = list(a), list(b)
    for i in range(len(n)):
        summ += retDist(a[i], b[i])
    return summ

mini = 0
result = []

# For every permutation in the list, find the distance between points and track the smallest
for x in li:
    n = [int(j) for j in x]
    res = sendPattern(n)
    result.append((res,n))

print(min(result)) # Print the smallest result
