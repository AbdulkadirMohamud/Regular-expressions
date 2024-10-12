import re
txt = 'I like to code daily Python and Javascript as well'
# It returns an object with span and match
match = re.match ('I like to code', txt,  re.I)
print(match ) # <re.match object; span=(0, 17), match='I like to code'>
# we can get the starting and ending position of the match as tuple using span
span = match.span()
print(span) # (0, 17)
# lets find the start and stop position of the match as tuple using span
start, end = span
print (start, end) # 0, 15
substring = txt[start:end]
print(substring) # I like to code

# search

txt = '''python is the most popular programming language that easy to understand is 
I suggest to learn python'''
# it returns a list 
matches = re.refindall ('python', txt)
print(matches) # ['python', 'python']

# writing RegEx Patterns

import re
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day will keep the doctor  far far away'
matches = re.findall ( regex_pattern, txt,  re. I)
print(matches) # ['Apple', 'apple']


