import re
# search(pattern, string)
# Пошук першої відповідності регулярному виразу в рядку.

string = "Hello, world!"
# string = "Hello, world! Bye."
pattern = r"(\w+), (\w+)!"
# pattern = r"\w+, \w+!"
match = re.search(pattern, string)
g=match.group()
g1=match.group(1)
g2=match.group(2)
# g3=match.group(3)
# index error

exit()

string = "Hello, world!"
match = re.search('world', string)
g=match.group()
sp=match.span()
