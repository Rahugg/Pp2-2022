import re
s = input()
pattern = "a.*b"
print("MATch") if (re.search(pattern,s)) else print("no")