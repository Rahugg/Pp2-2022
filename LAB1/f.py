n = int(input())
numbers_list = [] #emptry list with numbers
for i in range(0,n):
    numbers = int(input())
    numbers_list.append(numbers) #append - inputting them to list
for i in range (0,n):
    if numbers_list[i] <= 10:
        print ('Go to work!')
    elif numbers_list[i] > 10  and numbers_list[i] <= 25:
        print('You are weak')
    elif numbers_list[i] > 25 and numbers_list[i] <= 45:
        print('Okay, fine')
    else:
        print('Burn! Burn! Burn Young!')            
