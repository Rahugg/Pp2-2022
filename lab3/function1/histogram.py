def histogram(numbers,ans):
    for i in range(len(numbers)):
        ans.append('*'*numbers[i])
        
    print(*ans, sep = "\n")


numbers=list(map(int,input().split()))

histogram(numbers,[])