def unique(numbers,ans):
    for i in range(len(numbers)):
        if numbers[i] not in ans:
            ans.append(numbers[i])
    print(*ans)


numbers=list(map(int,input().split()))

unique(numbers,[])