def threeandfour(n):
    for i in range(n):
        if(i%3==0 and i%4==0):
            yield i
n = int(input("Input number: "))
for i in threeandfour(n):
    print(i, end = ' ')