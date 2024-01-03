from itertools import *

# `itertools.count(start=0, step=1)`
'''
for i in count(0, 2):
    if i >= 10:
        break
    else:
        print(i)

print('*****'*6)		
'''		
#### `itertools.cycle(iterable)`
'''
from time import sleep
seasons = ('winter', 'spring', 'summer', 'fall')
for season in cycle(seasons):
	print(season)
	sleep(2)
'''



#### `itertools.repeat(object[, times])`
'''
print(' '.join(repeat('crazy', 4)), 'world')
'''


### Комбінація значень
#### `itertools.combinations(iterable, r)`
'''
for c in combinations([1,2,3,4], 3):
	print(c)

keys = list(combinations('0123456789', 2))
print(' '.join(''.join(key) for key in keys))
'''



### Фільтрація послідовностей
#### `itertools.compress(data, selectors)`
'''
filtered = compress('bicycle', [1,0,0,1,0,0,1])
print(''.join(filtered))
'''


### Інші ітератори
#### `itertools.accumulate(iterable[, function])`

for i in accumulate([1, 2, 3, 4, 5, 6]):
	print(i)

print('*****'*6)		
















