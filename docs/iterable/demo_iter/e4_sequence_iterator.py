class Squares:
    def __init__(self, count):
        self.index_range = range(count)
    def __getitem__(self, index):
        if index in self.index_range:
            return (index+1)**2
        raise IndexError

i = iter(Squares(3))
# next(i)
l = list(Squares(10))
