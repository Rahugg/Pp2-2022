from math import sqrt

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self,x,y):
        return self.x,self.y
    def move(self,x,y):
        self.x+=x
        self.y+=y
        return self.x,self.y
    def dist(self,x2,y2):
        y1 = y2 - self.y
        x1 = x2 - self.x
        return sqrt(x1**2 + y1**2)

x,y = map(int, input().split())
f=Point(x,y)
x2,y2 = map(int,input().split())
f2=Point(x2,y2)

print(f.show(x,y))
print(f.move(x2,y2))
print(f.dist(x2,y2))
