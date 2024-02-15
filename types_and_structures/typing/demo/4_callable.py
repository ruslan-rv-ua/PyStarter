class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, /, x):
        return x * self.factor
    
x2 = Multiplier(2)
x3 = Multiplier(3)

x2(5)
x3(5)