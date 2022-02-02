
sentence = input()
letter = input()
check = []
for i in range(len(sentence)):
    if letter in sentence[i]:
        check.append(i)
        break
for i in reversed(range(len(sentence))):
    if letter in sentence[i]:
        check.append(i)
        break
if check[0]==check[1]:
        print(check[0])
else:
    print(check[0], check[1])   