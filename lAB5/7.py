import re 
def lower_to_upper(s):
    return s.title()
snake = input()
camel = re.sub("_"," ",snake)
print(re.sub(" ","",lower_to_upper(camel)))