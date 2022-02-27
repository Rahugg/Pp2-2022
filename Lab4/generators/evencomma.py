from tkinter import N


def separated(n):
    for i in range(n):
        if(i%2==0):
            yield i
n = int(input("Input number: "))
values = []
for i in separated(n):
    values.append(str(i))

print (",".join(values))