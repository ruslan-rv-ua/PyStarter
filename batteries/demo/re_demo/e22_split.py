import re
# split(pattern, string, maxsplit=0)
# Розбиття рядка на частини за допомогою регулярного виразу

string = "apple, banana, cherry"
pattern = r',\s*'
# string = "apple,     banana, cherry"
p = re.split(pattern, string)
p = re.split(pattern, string, maxsplit=1)

# ??
string = "apple1 banana2 cherry3"
pattern = r'\d\s*'
p = re.split(pattern, string)
