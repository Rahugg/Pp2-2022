from cmath import pi
import math
sides = int(input('Input number of sides: '))
length = int(input('Input the length of a side: '))
s = (sides*length**2)/4*math.tan(pi/sides)
print(f'The area of the polygon is: {s}')