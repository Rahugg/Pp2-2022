s = input()

sequence = []

flag_correct = True

for bracket in s:
    if bracket == '(' or bracket == '[' or bracket == '{':
        sequence.append(bracket)
    elif sequence and (bracket == ')' or bracket == ']' or bracket == '}'):
        if (bracket == ')' and sequence[-1] == '(') or (bracket == ']' and sequence[-1] == '[') or (bracket == '}' and sequence[-1] == '{'):
            sequence.pop()
        else:
            flag_correct = False
            break
        
if sequence:
    flag_correct = False
print("Yes" if flag_correct == True else "No")