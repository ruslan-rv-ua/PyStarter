list(zip([1, 2, 3], ['a', 'b', 'c']))
list(zip([1, 2, 3], ['a', 'b', 'c'], ['x', 'y', 'z']))
list(zip('hello', [1, 2, 3, 4, 5]))
list(zip([], [1, 2, 3]))
list(zip([], [3]))
list(zip([1], [1, 2, 3]))

# from itertools import count

def count(start=0):
    while True:
        yield start
        start += 1

def Enumerate(iterable, start=0):
    for number, value in zip(count(start), iterable):
        yield number, value
        
r = list(Enumerate('asdf', 10))



sorted([3, 1, 4, 1, 5, 9, 2, 6, 5])
sorted("hello")
sorted("hello", reverse=True)


# ! reversed({1,2,3})
list(reversed([1, 2, 3, 4, 5]))
''.join(reversed("hello"))
list(reversed(range(5)))
