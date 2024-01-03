# Модуль `itertools`

Модуль містить функції для створення ефективних ітераторів, які довзволяють виконувати  ітерації по даним різними способами.

Усі функції у цьому модулі повертають ітератори, які можна використовувати в інструкції `for` та в інших функціях, де застосовуються ітератори, 
наприклад в функціях-генераторах і у виразах-генераторах.

Далі розглядаються деякі з функцій з модуля `itertools`. 
З повним вмістом модуля можна ознайомитись у документації.

## Нескінченна ітерація

За допомогою цих функцій можна генерувати об'єкти або виконувати певні дії необмежену кількість раз. 
Це означає, що ви самостійно маєте перервати ітерування.

### `itertools.count(start=0, step=1)`

Створює рівномірно розподілену послідовність, генеруючи об'єкти за допомогою одного або двох параметрів.  Першим аргументом тут буде стартове значення набора даних, а другим — довжина постійного кроку. 

	:::python
	>>> for i in count(0, 2):
	...     if i >= 10:
	...         break
	...     else:
	...         print(i)
	...
	0
	2
	4
	6
	8
	>>>

### `itertools.cycle(iterable)`

Створює ітератор, який в циклі багатократно виконує обхід елементів в об'єкті `iterable`.

	:::python
	>>> for season in cycle('winter spring summer fall'.split()):
	...     print(season)
	...
	winter
	spring
	summer
	fall
	winter
	spring
	summer
	fall
	winter
	...

	
### `itertools.repeat(object[, times])`

Створює ітератор, який багатократно відтворює об'єкт `object`. 
У необов'язковому аргументі `times` передається кількість повторень. 
Якщо цей аргумент не задано, кількість повторів буде нескінченною.

	:::python
	>>> print(' '.join(repeat('crazy', 4)), 'world')
	crazy crazy crazy crazy world
	>>>

## Комбінація значень

### `itertools.combinations(iterable, r)`

Усі можливі послідовності з `r` елементів, 
які взято з ітерабельного об'єкта `iterable`. 
Елементи буде розташовано у тому ж порядку, у якому вони зустрічаються у початковому об'єкті `iterable`.

	:::python
	>>> keys = list(combinations('0123456789', 2))
	>>> len(keys)
	45
	>>> print(' '.join(''.join(key) for key in keys))
	01 02 03 04 05 06 07 08 09 12 13 14 15 16 17 18 19 23 24 25 26 27 28 29 34 35 36 37 38 39 45 46 47 48 49 56 57 58 59 67 68 69 78 79 89
	>>>

### Інші функції

- combinations_with_replacement
- permutations
- product


## Фільтрація послідовностей

### `itertools.compress(data, selectors)`

Виконує фільтрацію послідовності `data`. 
Елемент повертається, тільки якщо відповідний елемент (з таким самим індексом) з послідовності `selectors` трактується як істина. 
Порівняння закінчується, коли досягнуто кінця однієї з послідовностей.

	:::python
	>>> filtered = compress('bicycle', [1,[],{},True,None,'','yes'])
	>>> print(''.join(filtered))
	bye
	>>>

### Інші функції

- filterfalse
- dropwhile
- takewhile

## Інші ітератори
	
### `itertools.accumulate(iterable[, function])`
	
На кожній ітерації повертає суму попередніх елементів послідовності. 
Початкове значення дорівнює 0. 

	:::python
	>>> for i in accumulate([1, 2, 3, 4, 5, 6]):
	...     print(i)
	...
	1
	3
	6
	10
	15
	21
	>>>
	
### `1(iterable[, function])`

### Інші функції

- chain.from_iterable
- starmap
- islice
- izip
- tee
- groupby

## Додаткові матеріали

- [Документація: модуль itertools](https://docs.python.org/3.7/library/itertools.html)
- [more-itertools](https://pypi.org/project/more-itertools/) — ще більше корисних ітераторів

<!--
https://all-python.ru/osnovy/itertools.html
http://www.ilnurgi1.ru/docs/python/modules/itertools.html
http://trainingweb.ru/page/iterate-module-itertools-python
-->





