---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Ітератори послідовностей

Пригадаємо: щоб об'єкт був ітерабельним, функція `iter()` має повернути ітератор для цього об'єкта. 
Якщо функція `iter()` не знаходить у потенційно ітерабельного об'єкта метода `__iter__()`,
але знаходить магічний метод `__getitem__()`, тоді Python спробує побудувати ітератор самостійно. 

Методу `__getitem__()` будуть передаватись цілі невід'ємні числа, тобто індекси для списків, які є невід'ємними (більші або дорівнюють нулю).
Ми повинні реалізувати повернення значення, що відповідає вказаному індексу.
Якщо переданий індекс виходить за межі (адже потрібно обмежити довжину послідовності), слід підняти виняток IndexError.

Створимо просту послідовність — квадрати перших 100 невід’ємних чисел:

```python
class Squares:
    def __getitem__(self, index):
        if index in range(100):
            return index * index
        raise IndexError
```

Тепер спробуємо отримати ітератор цієї послідовності та скористатися ним:

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
	
Коли ітератор досягає кінця послідовності, він піднімає виняток `StopIteration`, як і має робити ітератор.
