import re
# sub(pattern, repl, string, count=0)
# Заміна всіх відповідностей регулярного виразу в рядку на заданий рядок

string = "Hello, world! Hello, Python!"
pattern = r"Hello,\s*(\w+)!"
s = re.sub(pattern, r"Hi, \1!", string)


string = "apple1 banana2 cherry3"
pattern = r'\d'
s = re.sub(pattern, '', string)



string = "apple1 banana2 cherry3"
pattern = r'\d'
s = re.sub(pattern, '', string, count=1)

