# iterable

# iter()

i = iter([1,2,3])
i = iter('abc')

i = iter(range(1, 4))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))

###################

numbers = [1,2,3]
for n in numbers:
    print(n*n)
    
numbers = [1,2,3]
iterator = iter(numbers)
while True:
    try:
        n = next(iterator)
    except StopIteration:
        break
    print(n*n)
