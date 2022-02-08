x, y = input().split()
x, y = int(x), int(y)

n = int(input())
points = []

import math
for i in range(n):
    l = input()
    x1, y1 = l.split()
    dis = math.sqrt((int(x1) - x)**2 + (int(y1) - y)**2)
    points.append((l, dis))

points.sort(key = lambda x: x[1])

for i in points:
    print(i[0])