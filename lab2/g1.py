n = int(input())#demons

characters = {}

for x in range(n):
    a = input().split()
    if a[1] in characters:
        characters[a[1]] = int(characters[a[1]]) + 1 # all demon with same types
    else:
        characters[a[1]] = 1#new demon

m = int(input())# demon slayers

for x in range(m):
    a = input().split()
    if a[1] in characters:
        characters[a[1]] = int(characters[a[1]]) - int(a[2])#killing demons

ans = 0 

for x in characters:
    if characters[x] > 0:
        ans+=int(characters[x])#rest of the demons
print("Demons left: ", ans)        