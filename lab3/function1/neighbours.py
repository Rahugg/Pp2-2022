def has_33(numbers,n,ans):
    for i in range(n):
        if numbers[i] == 3:
            ans.append(numbers[i])
        else:
            if(len(ans) == 1):
                ans.pop()
    if len(ans) >= 2:
        print("True")
    else: 
        print("False")


numbers = list(map(int,input().split()))

has_33(numbers,len(numbers),[])
  