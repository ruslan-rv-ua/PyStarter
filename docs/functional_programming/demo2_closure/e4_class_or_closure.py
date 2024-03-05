class Averager:
    def __init__(self):
        self.count = 0
        self.total = 0

    def __call__(self, value):
        self.count += 1
        self.total += value
        return self.total / self.count
    

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