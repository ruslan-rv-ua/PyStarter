def countdown(n, message='go'):
    for count in range(n, 0, -1):
        yield count
    yield message

for count in countdown(3):
    print(count)