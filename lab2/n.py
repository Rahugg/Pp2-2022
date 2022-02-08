number = []
sums = []

while (1):
    num = int(input())
    if(num == 0):
        break
    number.append(num)
if len(number)%2==1:
    length = len(number)//2
    for i in range(length):
        sum = number[i]+number[-i-1]
        sums.append(sum)
    sums.append(number[len(number)//2])
    for i in range(len(sums)):
        print(sums[i], end = " ")

else:
    length = len(number)//2
    for i in range(length):
        sum = number[i]+number[-i-1]
        sums.append(sum)
    for i in range(len(sums)):
        print(sums[i], end = " ")
