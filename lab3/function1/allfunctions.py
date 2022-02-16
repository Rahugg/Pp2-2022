from math import pi
import random

def solve(numheads,numlegs):
    
    chicken = (4*numheads - numlegs)//2
    rabbit = numheads - chicken
    
    print(f'Rabbits are = {rabbit}')
    print(f'Chickens are = {chicken}')

def Guess_the_number(name,tries,check):

    guess = int(input("Take a guess.\n"))

    if(guess<check):
        print("\nYour guess is too low.")
    elif(guess>check):
        print("\nYour guess is too high.")
    else:
        print(f'Good job, {name} You guessed my number in {tries} guesses!')
        exit()

    Guess_the_number(name,tries+1,check)

def histogram(numbers,ans):
    for i in range(len(numbers)):
        ans.append('*'*numbers[i])
    print(*ans, sep = "\n")

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

def palindrome(str,n,rev__str):

    if(n==0):
        rev__str+=str[n]
        if(rev__str == str):
            print("True")
        else: 
            print("False")
    else:   
        rev__str+=str[n]#adding char

        palindrome(str,n-1,rev__str)

def permute(s, answer):
    if (len(s) == 0):
        print(answer, end = "  ")
        return
     
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)

def filter__prime(num__list):
    
    prime_list = []
    flag = False

    for i in range(len(num__list)):
        for j in range(2,num__list[i]//2+1):
            if(num__list[i]%j==0):#checking for prime
                flag = True
                break

        if flag == False and num__list[i] != 1: # adding to prime list
            prime_list.append(num__list[i])

        flag = False

    return prime_list

def reverse_string(str,n,rev__str):

    if(n==0):
        rev__str.append(str[n])
        print(*rev__str)
    else:   
        rev__str.append(str[n])#adding string

        reverse_string(str,n-1,rev__str)

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

def unique(numbers,ans):

    for i in range(len(numbers)):
        if numbers[i] not in ans:
            ans.append(numbers[i])

    print(*ans)

def volume(radius):
    print((4/3)*pi*radius**3)