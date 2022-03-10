import re 
s = input()
pattern = "^[a-z]+_[a-z]+$"
if(re.search(pattern,s)):
    print("MATCH!!!!!!!!")
else:
    print("No.")