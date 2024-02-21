def countdown(n):
    for count in range(n, 0, -1):
        yield count
    yield "Старт!"

for count in countdown(3):
    print(count)