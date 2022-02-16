def reverse_string(str,n,rev__str):

    if(n==0):
        rev__str.append(str[n])
        print(*rev__str)
    else:   
        rev__str.append(str[n])#adding string

        reverse_string(str,n-1,rev__str)


str = list(input().split())

reverse_string(str,len(str)-1,[])