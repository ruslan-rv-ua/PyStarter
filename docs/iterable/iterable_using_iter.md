Один з способів реалізувати ітератор полягає у визначенні магічних методів `__iter__()` і `__next__`.

Як вже зазначалось ітератор має реалізовувати магічний метод `__iter__()`, який має повертати сам ітератор. Зазвичай він виглядає так:

	:::python
	def __iter__(self):
		return self
		
Магічний метод `__next__` при кожному виклику має повертати чергове значення. Коли усі значення закінчаться, то при черговому і усіх наступних викликах цей метод має "піднімати" виняток `StopIteration`




### Лічилочка

Розглянемо на прикладі. Напишемо простий ітератор який реалізує "лічилочку", тобто перебирає усі цілі числа від 1 до вказаного значення включно.
 
	:::python
	class CountingOUt:
		def __init__(self, count_to):
			self.current = 1
			self.count_to = count_to
		def __iter__(self):
			return self
		def __next__(self):
			if self.current <= self.count_to:
				current = self.current
				self.current += 1
				return current
			else:
				raise StopIteration
				
Як це працює:

* у конструкторі ми запам'ятовуємо значення, до якого будемо рахувати, а також встановлюємо "поточне" значення, тобто починаємо з 1
* у магічному методі `__next__` повертаємо поточне значення лічилочки, якщо ми звісно ще не вийшли за межі лічби, і збільшуємо поточне значення на 1. У всіх інших випадках "піднімаємо" виняток `StopIteration`, що буде сигналізувати що лічити вже більше нічого.

Ну і спробуємо скористатись нашою лічилочкою:

	:::python
	>>> c = CountingOUt(5)
	>>> for n in c:
	...     print(n)
	...
	1
	2
	3
	4
	5
	>>>	


	
	
	
	
### Знову Фібоначчі!

Давайте реалізуємо генерацію чисел Фібоначчі за допомогою ітераторів. 

Задача: отримати послідовність з `N` чисел Фібоначчі:

	:::python
	class Fibo:
		def __init__(self, max_count):
			self.max_count = max_count
			self.count = 0
			self.first, self.second = 1, 1
		def __iter__(self):
			return self
		def __next__(self):
			self.count += 1
			if self.count > self.max_count:
				raise StopIteration
			elif self.count > 2:
				self.first, self.second = self.second, self.first + self.second
				return self.second
			else:
				return 1

				
Тепер можему зручно ітеруватись по послідовності Фібоначчі:

	:::python
	>>> for f in Fibo(8):
	...     print(f)
	...
	1
	1
	2
	3
	5
	8
	13
	21
	>>>
	
Створити список з послідовності Фібоначчі? Просто!:

	:::python
	>>> f = list(Fibo(7))
	>>> f
	[1, 1, 2, 3, 5, 8, 13]
	>>>
	
Щоб зрозуміти як це працює, давайте подивимось клас `list`:

	:::python
	>>> help(list)
	Help on class list in module builtins:

	class list(object)
	 |  list() -> new empty list
	 |  list(iterable) -> new list initialized from iterable's items
	 |
	 ...
	 ...
	 
Тут для нас цікаве наступне:

> list(iterable) -> new list initialized from iterable's items

тобто якщо конструктору передати ітерабельний об'єкт, то буде створено список з елементів цього ітерабельного об'єкта.
	
