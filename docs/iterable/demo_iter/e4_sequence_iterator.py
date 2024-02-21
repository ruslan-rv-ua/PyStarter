class Quads:
    def __getitem__(self, index):
        if index in range(100):
            return index * index
        raise IndexError

quads_iterator = iter(Quads())
