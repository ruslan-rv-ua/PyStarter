import re

'''
string = "Hello, world!"
pattern = r"(\w+), (\w+)"
match = re.search(pattern, string)
g=match.group()
g1=match.group(1)
g2=match.group(2)
s=match.start()
e=match.end()
'''

string = "Hello, world!"
match = re.search('world', string)
g=match.group()
sp=match.span()


