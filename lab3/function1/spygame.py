def spygame(nums,ans,check):

    stra = ""

    for i in range(len(nums)):
        if(nums[i]==0 or nums[i]==7):
            ans.append(nums[i])

    for i in range(len(ans)):
        stra+=str(ans[i])
        
    if check in stra:
        print("True")
    else:
        print("False")


nums = list(map(int,input().split()))

spygame(nums,[],"007")