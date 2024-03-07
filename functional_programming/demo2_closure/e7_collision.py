def adder(base):
    # def add(n):
        # return base + n
    return lambda n: base + n
    return add
    
f = adder(10)
r=f(1)



ff = [adder(base) for base in range(10, 31, 10)]
'''
for f in ff:
    print(f(1))
'''
print(*map(lambda f:f(1), ff))
print()

'''
ff = [lambda n: base+n for base in range(10, 31, 10)]
for f in ff:
    print(f(1))
'''

def create_adders():
    adders = []
    # return lambda n: base + n
    # adders = [add for base in range(10, 31, 10)]
    for base in range(10, 31, 10):
        adders.append(lambda n: base + n)
    return adders
    
ff = create_adders()
'''
for f in ff:
    print(f(1))
'''
print(*map(lambda f:f(1), ff))

print(*map(lambda f:f.__closure__, ff), sep='\n')