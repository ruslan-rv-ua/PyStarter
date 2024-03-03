s=', '.join(map(str, range(10)))

#############################

string = '1 2 5 3 8 9 4 11 44 77 15 18'

numbers = list(map(int, string.split()))

# filtered = list(filter(lambda x: x % 2 == 0, numbers))
filtered = list(filter(lambda x: x % 2 == 0, map(int, string.split())))

###########################################
# Додавання елементів двох списків:
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
# r = list(map(lambda t: t[0]+t[1], zip(numbers1, numbers2)))
r = list(map(lambda x, y: x + y, numbers1, numbers2))

from operator import add
r = list(map(add, range(5), filter(lambda x:x>4, range(10))))
