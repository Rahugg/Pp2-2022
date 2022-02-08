
    #DOESN'T WORK ON TEST 6

from math import sqrt

req1, req2 = input().split()
req1, req2= int(req1), int(req2) 

n = int(input())

points_collec = {}

for x in range(n):
    points = input().split()
    x1 = (abs(int(points[0])-req1))**2
    y1 = (abs(int(points[1])-req2))**2
    i = sqrt( x1 + y1 )#closest point formula
    points_collec[i] = points #making "i" as a key

sorted_points = sorted(points_collec.keys())#sorting them to the list

for x in sorted_points:
    print(points_collec[x][0], points_collec[x][1]) #printing the values from collection
    
    
   #DOESN'T WORK ON TEST 6
