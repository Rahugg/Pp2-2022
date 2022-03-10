from cgitb import text
import re
def text_match(text):
    patterns = 'ab{2,3}'
    if re.search(patterns,  text):
                return 'Found a match!'
    else:
                return('Not matched!')

s = input()
print(text_match(s))