def iter_lists(list1, list2):
    for item in list1:
        yield item
    for item in list2:
        yield item

def iter_lists(list1, list2):
    yield from list1
    yield from list2

def chain_iterables(*iterables):
    for iterable in iterables:
        yield from iterable
        
r = list(chain_iterables(
    [42, 'Hello'],
    'abc',
    range(1,5)
))