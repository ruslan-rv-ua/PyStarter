---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Створення ітераторів

Як вже зазначалось ітератор має реалізовувати магічні методи `__iter__()` та `__next__`.

Метод `__iter__()` має повертати сам ітератор. Зазвичай він виглядає так:

```python
def __iter__(self):
	return self
```		

Магічний метод `__next__` при кожному виклику має повертати чергове значення. 
Коли усі значення закінчаться, то при черговому і усіх наступних викликах цей метод має "піднімати" виняток `StopIteration`

### Лічилочка

Розглянемо на прикладі. 
Напишемо простий ітератор який реалізує "лічилочку", 
тобто перебирає усі цілі числа від 1 до вказаного значення включно.
 
```python
class CountingOut:
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
```				

Як це працює:

* у конструкторі ми запам'ятовуємо значення, до якого будемо рахувати, а також встановлюємо "поточне" значення, тобто починаємо з 1
* у магічному методі `__next__` повертаємо поточне значення лічилочки, якщо ми звісно ще не вийшли за межі лічби, і збільшуємо поточне значення на 1. У всіх інших випадках "піднімаємо" виняток `StopIteration`, що буде сигналізувати що лічити вже більше нічого.

Ну і спробуємо скористатись нашою лічилочкою:

	>>> c = CountingOut(5)
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

```python
class Fibonacci:
    def __init__(self, count):
        self._count = count
        self._a = 1
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == 0:
            raise StopIteration
        item = self._a
        self._a, self._b = self._b, self._a + self._b
        self._count -= 1
        return item
```
				
Тепер можему зручно ітеруватись по ряду Фібоначчі:

	>>> for f in Fibonacci(10):
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
	34
	55
	>>>

Треба створити список з чисел Фібоначчі? Не є питань:

	>>> list(Fibonacci(10))
	[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
	>>>

Клас `Fibonacci` є:

- ітератором, тому що реалізує методи `__iter__()` та `__next__()`;
- ітерабельним, тому що реалізує метод `__iter__()` який повертає ітератор.

Проітеруватись по такому ряду чисел Фібоначчі можна лише один раз:

	>>> fibo5 = Fibonacci(5)
	>>> list(fibo5)
	[1, 1, 2, 3, 5]
	>>> list(fibo5)
	[]
	>>>

Виправимо цей "недолік": створимо окремо клас, який буде представляти ряд чисел Фібоначчі, і окремо ітератор по ньому.

```python
class FibonacciIterator:
    def __init__(self, count):
        self._count = count
        self._a = 1
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == 0:
            raise StopIteration
        item = self._a
        self._a, self._b = self._b, self._a + self._b
        self._count -= 1
        return item


class Fibonacci:
    def __init__(self, count):
        self._count = count

    def __iter__(self):
        return FibonacciIterator(self._count)

```

Тепер можна створити ряд чисел Фібоначчі необхідної довжини та ітеруватись по ньому скільки завгодно:

	>>> fibo5 = Fibonacci(5)
	>>> list(fibo5)
	[1, 1, 2, 3, 5]
	>>> list(fibo5)
	[1, 1, 2, 3, 5]
	>>>

