def myfunc(dishes,n,ans):
    if(n==len(dishes)):
        if ans >= 300:
            print('It is tasty!')
        else: 
            print ('Oh, no!')
    else:
        ans += ord(dishes[n])        
        return myfunc(dishes,n+1,ans)
dishes,ans,n = input(),0,0

myfunc(dishes=dishes,n=0,ans=0)

'''dishes = str(input())
answer = 0
for i in dishes:
    answer += ord(i)
if answer >= 300:
    print('It is tasty!')
else: 
    print ('Oh, no!')'''        