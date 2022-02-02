dishes = str(input())
answer = 0
for i in dishes:
    answer += ord(i)
if answer >= 300:
    print('It is tasty!')
else: 
    print ('Oh, no!')        