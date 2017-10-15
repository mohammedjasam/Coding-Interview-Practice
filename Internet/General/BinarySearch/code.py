a = [1,23,5,4,65,7,9,8,6,3,2,10,11,22,3235,67,8,3,3,1,23,32,5,34,7568,785,65,345,234]

a = sorted(list(set(a)))
print(a)

find = 345

def searchh(a, find):
    size = len(a)
    mid = round(size/2)
    print(a[:mid],a[mid], a[mid+1:])
    if a[mid] == find:
        print("found " + str(a[mid]))
    else:
        if find < a[mid]:
            a = a[:mid]
            searchh(a, find)
        else:
            a = a[mid+1:]
            searchh(a, find)

searchh(a, find)
