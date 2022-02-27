def down(n):
    for i in range(n,-1,-1):
        yield i
n = int(input('Input number: '))
for i in down(n):
    print(i, end = ' ')
