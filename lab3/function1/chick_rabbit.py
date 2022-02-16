def solve(numheads,numlegs):
    
    chicken = (4*numheads - numlegs)//2
    rabbit = numheads - chicken
    
    print(f'Rabbits are = {rabbit}')
    print(f'Chickens are = {chicken}')


numlegs,numheads = list(map(int,input().split()))

solve(numheads,numlegs)