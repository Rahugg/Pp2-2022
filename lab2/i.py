n = int(input())
books = []
cnt=0
for i in range(n):
    x = input().split()
    if(int(x[0])==1):
        books.append(x[1])
    else:
        cnt+=1
for i in range(cnt):
    print(books[i], end = " " )