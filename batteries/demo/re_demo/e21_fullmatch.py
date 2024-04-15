import re
# fullmatch(pattern, string)
# Перевірка, чи відповідає цілий рядок регулярному виразу.

string = "Hello, world!"
pattern = r"(\w+), (\w+)!"
# pattern = r"\w+, \w+!"
match = re.fullmatch(pattern, string)
g=match.group()
g1=match.group(1)
g2=match.group(2)



pattern = r'\w+'
match = re.fullmatch(pattern, string)
search = re.search(pattern, string)
