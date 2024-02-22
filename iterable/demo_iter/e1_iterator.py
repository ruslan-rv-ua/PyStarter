# iterable

# iter()

i = iter([1,2,3])
i = iter('abc')

i = iter(range(1, 4))
r1=next(i)
r2=next(i)
r3=next(i)
# r4=next(i)

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

###################

iter() __iter__
next() __next__