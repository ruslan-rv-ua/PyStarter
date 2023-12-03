---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Методи списків

Оскільки `list` — мутабельний тип даних, 
методи списків можуть змінювати сам список, до якого вони були використані. 

## append()

	lst.append(x)

Додає об'єкт "x" в кінець списку "lst"

	>>> l = [1,2,3]
	>>> l.append('add me!')
	>>> l
	[1, 2, 3, 'add me!']
	>>> l.append([4,5,6])
	>>> l
	[1, 2, 3, 'add me!', [4, 5, 6]]
	>>>

Повертає `None`.

## extend()

	lst.extend(x)

Додає усі елементи послідовності "x" в кінець списку "lst"

	>>> l = [1,2,3]
	>>> l.extend((4, 5, 6))
	>>> l
	[1, 2, 3, 4, 5, 6]
	>>> l = [1]
	>>> l.extend('add')
	>>> l
	[1, 'a', 'd', 'd']
	>>>

Повертає `None`.

## insert()

	lst.insert(i, x)

Вставляє у список у позицію з індексом "i" об'єкт "x".

	>>> l = [1, 2, 3, 2, 4]
	>>> l.insert(0, 'begin')
	>>> l
	['begin', 1, 2, 3, 2, 4]
	>>> l.insert(-1, 'end')
	>>> l
	['begin', 1, 2, 3, 2, 'end', 4]
	>>> l.insert(1000, 'nothing')
	>>> l
	['begin', 1, 2, 3, 2, 'end', 4, 'nothing']
	>>> l.insert(-1000, 'so far')
	>>> l
	['so far', 'begin', 1, 2, 3, 2, 'end', 4, 'nothing']
	>>>
	
Повертає `None`.
	
## remove()

	lst.remove(x)

Видаляє зі списка "lst" перший елемент зі значенням "x".

	>>> l = [1, 2, 3, 2, 4]
	>>> l.remove(2)
	>>> l
	[1, 3, 2, 4]
	>>> l.remove(777)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: list.remove(x): x not in list
	>>>

Повертає `None`.

## pop()

	lst.pop(i)

Видаляє зі списка "lst" елемент з індексом "i" і повертає його.
Якщо "i" не вказано — видаляє і повертає останній елемент.

	>>> l = [1, 2, 3, 4, 5]
	>>> l.pop(3)
	4
	>>> l
	[1, 2, 3, 5]
	>>> l.pop()
	5
	>>> l
	[1, 2, 3]
	>>> l.pop(3)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	IndexError: pop index out of range
	>>>

## index()
	
	lst.index(x)

Повертає індекс першого входження елемента зі значенням "x" у списку "lst".

	>>> l = [1, 2, 3]
	>>> l.index(2)
	1
	>>> l.index(777)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: 777 is not in list
	>>>

## count()
	
	lst.count(x)

Повертає кількість елементів зі значенням "x" у списку "lst".

	>>> l = [1, 2, 3, 2, 3, 3]
	>>> l.count(3)
	3
	>>> l.count(777)
	0
	>>>

## sort()
	
	lst.sort()

Сортування списку "lst".

	>>> l = [1, 7, 2, 6, 3, 5, 4]
	>>> l.sort()
	>>> l
	[1, 2, 3, 4, 5, 6, 7]
	>>>

Повертає `None`.

## clear()
	
	lst.clear()

Видаляє усі елементи зі списку "lst".

	>>> l = [1, 7, 2, 6, 3, 5, 4]
	>>> l.clear()
	>>> l
	[]
	>>>

Повертає `None`.

## reverse()

	lst.reverse()

"Перевертає" порядок елементів списка.

	>>> l = [1, 10, 5]
	>>> l.reverse()
	>>> l
	[5, 10, 1]
	>>>

Повертає `None`.

