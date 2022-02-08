num = int(input())
arr = []
for x in range(num):
    elements = []
    for y in range(num):
        if(x==0):
            elements.append(y)
        elif(x==y):
            elements.append(x*y)
        elif(y==0):
            elements.append(x)
        else:
            elements.append(0)
    arr.append(elements)
for x in range(num):
    for y in range(num):
        print(arr[x][y], end = " ")
    print()