def fibonacci_generator(count):
    a, b = 0, 1
    for _ in range(count):
        yield b
        a, b = b, a + b
        # temp = a
        # a = b
        # b = temp + b

r = list(fibonacci_generator(10))

