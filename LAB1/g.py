def myfunc(binnum,n,todec):
    if n==len(binnum):
        print(todec)
    else:
        todec += (ord(binnum[n])-48)*pow(2,len(binnum)-n-1)
        myfunc(binnum,n+1,todec)

binnum = input()
myfunc(binnum = binnum, n = 0, todec = 0)

'''
number = input()
print(int(number, 2))
'''