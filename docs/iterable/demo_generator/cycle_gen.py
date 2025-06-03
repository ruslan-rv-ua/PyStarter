def cycle(iterable):
    while True:
        yield from iterable

c = cycle('abc')
for i, val in enumerate(c):
    if i > 7:
        break
    print(val)
