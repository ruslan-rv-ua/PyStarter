def add(a,b):
    return a+b
    
r = add(*[2,3])
r = add(*range(3,5))

# print(*args, sep=' ', end='\n')
# print(*args, sep=' ', end='\n', file=None, flush=False)
data = (x*x for x in range(1, 5))
options = dict(sep=', ', end='\nбільше немає\n')
print(*data, **options)

##################################################

data = (x*x for x in range(1, 5))
l = ['почали', *data, 'закінчили']
# l = ['почали', *data, 'закінчили', *options]
