def counter(function):
    count = 0
    def f(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'function {function.__name__!r} was called {count} times')
        function(*args, **kwargs)
    return f
    
p = counter(print)
#p('hello', sep=' ')
#p(*'hello', sep=' ')

print(p.__code__.co_freevars, sep='\n')
# print(*p.__closure__, sep='\n')
