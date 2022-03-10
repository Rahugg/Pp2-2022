import re 

camel = input()
pattern =r"(.+?)([A-Z])"
def camel_to_snake(s):
    return s.group(1).lower()+'_'+s.group(2).lower() 

print(re.sub(pattern,camel_to_snake,camel))
