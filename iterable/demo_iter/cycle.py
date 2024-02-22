class Cycle:
    def __init__(self, iterable):
        self.items = list(iterable)
        self.index = 0

    def __next__(self):
        item = self.items[self.index % len(self.items)]
        self.index += 1
        return item

    def __iter__(self):
        return self


i = Cycle('abc')
for _ in range(10):
    print(next(i))

class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)

    def __next__(self):
        try:
            item = next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            item = next(self.iterator)
        return item

    def __iter__(self):
        return self

print()
i = Cycle('abc')
for _ in range(10):
    print(next(i))
