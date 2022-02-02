n = int(input())
mail="@gmail.com"
mails_list=[]
for i in range(0,n):
    check = input()
    if mail in check:
        elements = check.strip("@gmail.com")
        if(check[len(check)-1] == 'm'):
            mails_list.append(elements)
for i in range(0,len(mails_list)):
    print(mails_list[i])