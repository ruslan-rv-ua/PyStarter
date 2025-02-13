string = 'Привіт'
s = string[0]
print(s)

s = '12345'[4]
print(s)

# s = '12345'[5]
# IndexError: string index out of range
print(s)

s = '12345'[-1]
s = '12345'[-5]
# s = '12345'[-6]
# s = '12345'[4/2]
# TypeError: string indices must be integers, not 'float'
print(s)

# slice
s = '0123456789'[0:5]
s = '0123456789'[:5]
print(s)

s = '0123456789'[5:10]
s = '0123456789'[5:]
s = '0123456789'[5:0]
print(s)

s = '0123456789'[1:-1]
print(s)

# step
s = '0123456789'[1:-1:2]
s = '0123456789'[::3]
s = '0123456789'[::-1]
print(s)

# звертати увагу на типи!
