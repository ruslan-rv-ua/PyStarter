def fibonacci_generator(count):
    a, b = 0, 1
    for _ in range(count):
        yield b
        a, b = b, a + b

l = list(fibonacci_generator(10))

class Fibonacci:
    def __init__(self, count):
        self.count = count
        
    def __iter__(self):
        return self.fibonacci_generator1(self.count)

    @staticmethod
    def fibonacci_generator1(count):
        a, b = 0, 1
        for _ in range(count):
            yield b
            a, b = b, a + b
f5=Fibonacci(5)
l1 = list(f5)
l2 = list(f5)