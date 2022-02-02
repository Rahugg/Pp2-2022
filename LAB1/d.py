number,z = int(input()),input()
if z == 'k':
    floating = int(input())
    answer = number/1024
    print(round(answer,floating))
else:
    print(number*1024)    
