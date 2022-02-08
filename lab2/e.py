n = input()
arr = []
if(len(n)<=2):
    k = int(input())
    for x in range(int(n)):
        arr.append(k+2*x)
    xorresult = arr[0]
    for x in range(1,int(n)):
        xorresult ^= arr[x]
    print (xorresult)

else:
    n1 = n.split()
    for x in range(int(n1[0])):
        arr.append(int(n1[1])+2*x)
    xorresult = arr[0]
    for x in range(1,len(arr)):
        xorresult ^= arr[x]
    print (xorresult)