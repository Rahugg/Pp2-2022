def squares(a,b):
    for i in range(a,b):
        yield i**2

a,b = map(int,input("input a and b: ").split())
for i in squares(a,b):
    print(i, end = " ")