def palindrome(str,n,rev__str):

    if(n==0):
        rev__str += str[n]
        if(rev__str == str):
            print("True")
        else: 
            print("False")
    else:   
        rev__str += str[n]#adding char

        palindrome(str,n-1,rev__str)


str = input()

palindrome(str,len(str)-1,"")