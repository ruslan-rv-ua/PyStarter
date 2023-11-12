a = 999
b = 999
print(a is b)
b = int(str(999))


# r = id(a)
r = id(a) == id(b)
r = a is b

