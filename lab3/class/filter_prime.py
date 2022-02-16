def prime(x):
    if x == 1:
            return False
    elif x == 0:
            return False
    for j in range(2,int((x**0.5))+1):
        if x % j == 0:
            return False
    return True

numbers = list(map(int,input().split()))
y = list(filter(lambda x:prime(x),numbers))
print(*y)