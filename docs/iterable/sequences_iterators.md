---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Ітератори послідовностей

Пригадаємо: щоб об'єкт був ітерабельним, функція `iter()` має повернути ітератор для цього об'єкта. 
У свою чергу якщо функція `iter()` не знаходить у потенційно ітерабельного об'єкта метода `__iter__()`, 
але знаходить магічний метод `__getitem__()`, тоді Python спробує побудувати ітератор самостійно. 

Методу `__getitem__()` будуть передаватись цілі невід'ємні числа, тобто як індекси для списків, але які більше або дорівнюють нулю. 
Ми ж у свою чергу повинні реалізувати повернення необхідного значення, яке відповідає вказаному індексу. 
Якщо переданий "індекс" виходить за межі, атже нам треба ж якимось чином обмежити довжину послідовності, то ми маємо "підняти" виняток IndexError


Створимо просту послідовність — квадрати перших 100 невід'ємних чисел:

```python
class Squares:
    def __getitem__(self, index):
        if index in range(100):
            return index * index
        raise IndexError
```

Тепер спробуємо отримати ітератор цієї послідовності:

	>>> squares_iterator = iter(Squares())
	>>> next(squares_iterator)
	0
	>>> next(squares_iterator)
	1
	>>> next(squares_iterator)
	4
	>>> next(squares_iterator)
	9
	>>> while True: n = next(squares_iterator)
	...
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	StopIteration
	>>>
	
Ітератор при досягненні кінця послідовності "піднімає" виняток `StopIteration`, власне як і має робити ітератор. 
