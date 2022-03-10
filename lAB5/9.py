import re
s = input()
print(re.sub(r"(\w)([A-Z])", r"\1 \2", s))