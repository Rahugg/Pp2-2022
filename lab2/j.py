n = int(input())
capital,lower,number = False,False,False
strong = []

for x in range(n):
    password = input()
    for i in range(len(password)):
        if (password[i]>='A' and password[i]<= 'Z'):
            capital = True
        if (password[i]>='0' and password[i]<='9'):
            number = True
        if (password[i]>='a' and password[i]<='z'):
            lower = True
    if capital:
        if lower:
            if number:
                if password not in strong:
                    strong.append(password)
    capital,lower,number = False, False, False


strong.sort()
print(len(strong))

for i in strong:
    print(i)
