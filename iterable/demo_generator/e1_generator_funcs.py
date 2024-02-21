def generator_function():
    print('* start')
    yield "Hello"
    print('* middle')
    yield "PyStarter"
    print('* finish')
    
    
# generator_function
g = generator_function()
# g
# g.__iter__
# g.__next__

r = next(g)
r = next(g)
# r = next(g)

for string in generator_function():
    print(string)