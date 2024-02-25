def generator_function():
    print('* почали')
    yield "перше"
    print('* продовжуємо')
    yield "друге"
    print('* закінчили')
    
    
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