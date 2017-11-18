def search(array, Sum):
    comp = []

    for x in array:
        if x not in comp:
            comp.append(Sum - x)
        if x in comp:
            print(Sum - x, x)


search([4,2,3,1], 6)
