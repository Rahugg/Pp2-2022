import string
alphabet= string.ascii_lowercase
for letter in alphabet:
    with open(letter+".txt",'w') as file:
        file.write(letter)