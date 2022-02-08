n = int(input())

students = {}

for x in range(n):
    student, money = input().split()#to print 2 values in one line
    if student in students:
        students[student] = int(students[student]) + int(money) #summarizing the values
    else:
        students[student] = int(money) #adding new key

maxi = max(students.values())#maximum

sortedstudents = sorted(students.keys())#sorting by keys

for x in sortedstudents:
    if students[x] == maxi:
        print(x, " is lucky!")
    else:
        print(x, " has to receive ", maxi - int(students[x]), " tenge")