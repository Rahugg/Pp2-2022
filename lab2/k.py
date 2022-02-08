s = input()
s = s.replace(',', '').replace('!', '').replace('?', '').split()

unique = []

for word in s:
    if word not in unique:
        unique.append(word)

unique.sort()

print(len(unique))
print(*unique, sep = '\n')