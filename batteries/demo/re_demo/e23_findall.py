import re
# findall(pattern, string)
# Пошук усіх відповідностей регулярного виразу в рядку

string = "Hello, world! Hello, Python!"
pattern = r"Hello, (\w+)!"
l = re.findall(pattern, string)

string = "Hello, world; hello, Python!"
pattern = r"Hello, (\w+)[!;]"
l = re.findall(pattern, string, flags=re.IGNORECASE)


# also
# finditer(pattern, string)
