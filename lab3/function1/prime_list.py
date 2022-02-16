
def filter__prime(num__list):
    
    prime_list = []
    flag = False

    for i in range(len(num__list)):
        if(num__list[i]==0):
                flag = True
        elif(num__list[i]==1):
                flag = True
        for j in range(2,int((num__list[i]**0.5))+1):
            if(num__list[i]%j==0):#checking for prime
                flag = True
                break
        if flag == False and num__list[i] != 1: # adding to prime list
            prime_list.append(num__list[i])

        flag = False

    return prime_list


num__list = list(map(int,input().split()))

print(*filter__prime(num__list))
