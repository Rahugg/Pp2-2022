def gensquares(n):
    for i in range(n):
        yield i**2

n = int(input("Input number: "))
for x in gensquares(n):
    print (x)