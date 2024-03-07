class Averager:
    def __init__(self):
        self._count = 0
        self._total = 0

    def __call__(self, value):
        self._count += 1
        self._total += value
        return self._total / self._count
    

a = Averager()
a(10)
a(20)
a(30)

def averager():
    count = 0
    total = 0
    def add(value):
        nonlocal count, total
        count += 1
        total += value
        return total / count
    return add


a = averager()
a(10)
a(20)
a(30)