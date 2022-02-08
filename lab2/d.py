n = int(input())
arr = []
if(n%2==0):
    for x in range(n):
        elements = []
        for y in range(n):
            if(y>x):
                elements.append('.')
            else: 
                elements.append('#')
        arr.append(elements)
else:
    for x in range(n):
        elements = []
        for y in range(n):
            if(x+y<n-1):
                elements.append('.')
            else:
                elements.append('#')
        arr.append(elements)
for x in range(n):
    for y in range(n):
        print(arr[x][y], end = "")
    print()
        