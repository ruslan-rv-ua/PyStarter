import re
# compile(regexp: str, flags: int)

string = "apple1 banana2 cherry3"
regex = re.compile(r'\d')
s = regex.sub('', string, count=1)
