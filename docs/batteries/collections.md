# Модуль collections

<!-- https://realpython.com/python-collections-module/ -->

В стандартній бібліотеці є модуль `collections`. 
Як можна здогадатись з назви, там знаходяться реалізації певних контейнерів. 

|Тип даних|Опис|
|-|-|
|[deque](https://docs.python.org/3/library/collections.html#collections.deque)|стеки і черги|
|[defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)|словник з дефолтними значеннями|
|[namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)|кортеж з атрибутами|
|[OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict)|впорядкований словник|
|[Counter](https://docs.python.org/3/library/collections.html#collections.Counter)|лічильник об'єктів|
|[ChainMap](https://docs.python.org/3/library/collections.html#collections.ChainMap)|об'єднання декількох відображень|

Крім того є класи 
[UserDict](https://docs.python.org/3/library/collections.html#collections.UserDict), 
[UserList](https://docs.python.org/3/library/collections.html#collections.UserList) та 
[UserString](https://docs.python.org/3/library/collections.html#collections.UserString). 
Це класи-обгортки до відповідних "стандартних" типів даних. 
Успадковуйтесь від цих класів якщо вам знадобиться додати функціонал до вже існуючого типу даних. 

Дуже часто можливості модуля `collections` залишаються недооціненими. 
Рекомендуємо детально ознайомитись з відповідною документацією, 
швидше за все час від часу вам буде корисним цей модуль. 

Далі ж ми дуже коротко розглянемо лише самі "визначні" на думку автора можливості цього модуля. 

## namedtuple

Іменований кортеж. 
Дозволяє отримати доступ до об'єктів як до атрибутів через визначене ім'я. 
Можна розглядати як альтернативу класів-контейнерів даних. 
Порівняно зі "звичайними" кортежами суттєво підвищує читабельність початкового кода. 
Порівняно з класами займають меньше місця і працюють швидше. 

Створити іменований кортеж:

	namedtuple(type_name, field_names)
	
- `type_name` — ім'я нового типу даних, який, власне, створюється. Символьний рядок з валідним ідентифікатором. 
- `field_names` — імена полів, що будуть використовуватись. Можна задати як:
	- ітерабельний об'єкт символьних рядків
	- символьний рядок з розділеними пробілом іменами
	- символьний рядок з розділеними комою іменами
	
Приклади:

	:::python
	>>> from collections import namedtuple
	>>> Point = namedtuple('Point', ['x', 'y'])
	>>> p = Point(2, 5)
	>>> p
	Point(x=2, y=5)
	>>> p.x
	2
	>>> p.y
	5
	>>> p[0]
	2
	>>> Point = namedtuple('Point', 'x, y')
	>>> Point(1, 3)
	Point(x=1, y=3)
	>>> Point = namedtuple('Point', 'x y')
	>>> Point(7, 8)
	Point(x=7, y=8)
	>>> # namedtuple — немутабельний:
	>>> Point(7, 8).x
	7
	>>> Point(7, 8).x = 1
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: can't set attribute
	>>> # дефолтні значення полів:
	>>> Person = namedtuple('Person', 'name job', defaults = ['Python Developer'])
	>>> p = Person('Jane')
	>>> p
	Person(name='Jane', job='Python Developer')
	>>> # швидко отримати словник з іменованого кортежа:
	>>> p._asdict()
	{'name': 'Jane', 'job': 'Python Developer'}
	>>> створити поверхневу копію і замінити значення поля:
	>>> p._replace(job='Web Developer')
	Person(name='Jane', job='Web Developer')
	>>>
	>>> Person._make(['Alice', 'HR'])
	Person(name='Alice', job='HR')
	>>>

Зауважте: імена деяких методів починаються з символа підкреслення, 
але є частиною відкритого інтерфейса. 
Це зроблено для того, щоб уникнути колізій з іменами які визначатиме розробник. 

## defaultdict

Спроба отрлимати значення зі словника по неіснуючому ключу призводить до відповідної помилки: 

	:::python
	>>> favorites = {'fruit': 'apple'}
	>>> favorites['language']
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'language'
	>>>

Можна скористатись методом `get()`, але після цього словник не змінюється, 
тобто нова пара ключ-значення не додається: 

	:::python
	>>> favorites.get('language', 'Python')
	'Python'
	>>> favorites
	{'fruit': 'apple'}
	>>>

Клас `defaultdict` дозволяє створити словник з дефолтними значеннями для неіснуючих ключів. 
Конструктор приймає об'єкт-функцію. 
Коли відбувається доступ по неіснуючому ключу, 
вказана функція викликається без аргументів, 
вона має повернути дефолтне значення. 

	:::python
	>>> from collections import defaultdict
	>>> counter = defaultdict(int)
	>>> counter
	defaultdict(<class 'int'>, {})
	>>> counter['dogs']
	0
	>>> counter
	defaultdict(<class 'int'>, {'dogs': 0})
	>>> counter['dogs'] += 2
	>>> counter['cats'] += 7
	>>> counter
	defaultdict(<class 'int'>, {'dogs': 2, 'cats': 7})
	>>> counter['cats']
	7
	>>>


## OrderedDict

`OrderedDict` — це словник, який "пам'ятає" порядок додавання пар ключ-значення. 
Ітерування по такому словнику буде відбуватись у тому порядку, 
у якому елементи додавались в нього. 

	:::python
	>>> from collections import OrderedDict
	>>> life_stages = OrderedDict()
	>>> life_stages["childhood"] = "0-9"
	>>> life_stages["adolescence"] = "9-18"
	>>> life_stages["adulthood"] = "18-65"
	>>> life_stages["old"] = "65+"
	>>> for stage, years in life_stages.items():
	...     print(f'{stage} - {years}')
	...
	childhood - 0-9
	adolescence - 9-18
	adulthood - 18-65
	old - 65+
	>>>

Довгий час тип даних `dict` мав реалізацію як невпорядкованого контейнера. 
В Python 3.6 реалізацію цього класа було повністю переопрацьовано, 
словники стали більш швидкими і займати меньший об'єм пам'яті. 
Разом з цим словники "неочікувано" стали впорядкованими. 
Починаючи з Python 3.7 це офіційно зафіксовано у документації. 
Але не дивлячись на вищесказане коли треба впорядкований словник, 
рекомендується все ж таки використовувати `OrderedDict`. 
Причини наступні:

- назва класа явно вказує на впорядкованість контейнера, це покращує читабельність 
- `OrderedDict` має додаткові методи для керування порядком пар ключ-значення 

Приклади:

	:::python
	>>> letters = OrderedDict(b=2, d=4, a=1, c=3)
	>>> letters
	OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])
	>>> # Перекинемо b в кінець
	>>> letters.move_to_end("b")
	>>> letters
	OrderedDict([('d', 4), ('a', 1), ('c', 3), ('b', 2)])
	>>> # Перекинемо b на початок
	>>> letters.move_to_end("b", last=False)
	>>> letters
	OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])
	>>> # відсортуємо словник по ключам
	>>> for key in sorted(letters):
	...     letters.move_to_end(key)
	...
	>>> letters
	OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
	>>>
	
Ще однією відмінністю `OrderedDict` від "звичайних" словників є спосіб порівняння двох об'єктів на рівність: 

	:::python
	>>> # в dict порівнюється лише вміст:
	>>> letters_0 = dict(a=1, b=2, c=3, d=4)
	>>> letters_1 = dict(b=2, a=1, d=4, c=3)
	>>> letters_0 == letters_1
	True
	>>> # в OrderedDict порівнюються вміст і порядок:
	>>> letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
	>>> letters_1 = OrderedDict(b=2, a=1, d=4, c=3)
	>>> letters_0 == letters_1
	False
	>>> letters_2 = OrderedDict(a=1, b=2, c=3, d=4)
	>>> letters_0 == letters_2
	True
	>>>
	
## Counter

Підрахунок кількості об'єктів — доволі часта задача. 
Зручно робити це дозволяє клас `Counter`. 
Достатньо передати йому будь-який ітерабельний об'єкт: 

	:::python
	>>> c = Counter('абракадабра')
	>>> c
	Counter({'а': 5, 'б': 2, 'р': 2, 'к': 1, 'д': 1})
	>>> c['а']
	5
	>>> c['б']
	2
	>>> n = Counter([4, 3, 2, 1, 3, 2, 1, 2, 1, 1])
	>>> n
	Counter({1: 4, 2: 3, 3: 2, 4: 1})
	>>> n[4] += 3
	>>> n
	Counter({4: 4, 1: 4, 2: 3, 3: 2})
	>>> n.update({1:7})
	>>> n
	Counter({1: 11, 4: 4, 2: 3, 3: 2})
	>>>

Отримати "найчастіші" об'єкти:

	:::python
	>>> n.most_common()
	[(1, 11), (4, 4), (2, 3), (3, 2)]
	>>> n.most_common(2)
	[(1, 11), (4, 4)]
	>>>
	
Зауважте: підраховувати можна лише об'єкти, що хешуються:

	:::python
	>>> Counter([[1], [2]])
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "C:\python38\lib\collections\__init__.py", line 552, in __init__
		self.update(iterable, **kwds)
	  File "C:\python38\lib\collections\__init__.py", line 637, in update
		_count_elements(self, iterable)
	TypeError: unhashable type: 'list'
	>>>
	
Клас `Counter` має ще багато корисних можливостей. 
Ознайомитись з усіма можна у відповідній документації.

