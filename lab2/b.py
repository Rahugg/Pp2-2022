num = int(input())
numbers = list(map(int, input().split()))
num1 = max(numbers)
numbers.remove(num1)
num2 = max(numbers)
print(num1*num2)