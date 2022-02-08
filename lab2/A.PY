def Possiblejump(nums):
    n = len(nums)
    Maxreach = 0
    for i in range(n):
        if i>Maxreach or Maxreach >=n-1:
            break
        else:
            Maxreach = max(Maxreach, i + nums[i])
    if Maxreach < n-1:
        return False
    else:
        return True

n = input().split()
nums = []
for i in n:
    nums.append(int(i))
print(1) if Possiblejump(nums) else print(0)    