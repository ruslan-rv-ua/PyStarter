def fib(n):
    # print(f'fib({n})')
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

r=fib(30)
# r=fib(35)
exit()

def fib(n, level=0):
    print(f'{" "*level*4}fib({n})')
    if n == 1 or n == 2:
        return 1
    return fib(n-1, level+1) + fib(n-2, level+1)

fib(6)

############

def cached_fib():
    cache = {1:1, 2:1}
    def fib(n):
        if n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return fib

f = cached_fib()

######################

from functools import cache

@cache
def fib(n):
    # print(f'fib({n})')
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
v=fib(350)