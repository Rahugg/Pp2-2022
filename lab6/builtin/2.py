def upper_case(s):
    cnt = 0
    for x in s:
        if(x>='A' and x<='Z'):
            cnt+=1
    return cnt
def lower_case(s):
    cnt1 = 0
    for x in s:
        if(x>='a' and x<='z'):
            cnt1+=1
    return cnt1
s=input()
print(f'Uppercase letters: {upper_case(s)} ')
print(f'Lowercase letters: {lower_case(s)} ')