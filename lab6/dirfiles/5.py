from re import X


f = open("5.txt", "a")
s = ('a','b','c','d','e','f','g')
for x in s:
    f.write(x)
print(f.read())
