import re
s = input()
pattern = "[A-Z]+[a-z]+$"
print("MATch") if (re.search(pattern,s)) else print("no")