meters,cartridge= map(int, input().split())
ok=False
if meters < 500:
    if cartridge%2==0: 
        for i in range(2,meters//2) :
            if meters%i==0:
                print('Try next time!')  
                break
        else:
             print('Good job!')  
    else:
        print('Try next time!')
else:
    print('Try next time!')

