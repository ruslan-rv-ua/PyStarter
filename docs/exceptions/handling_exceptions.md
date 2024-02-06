---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

<!--
https://ru.stackoverflow.com/questions/1485541/Что-за-конструкция-raise-from-в-python
-->

# Обробка винятків

> ***Обробка виняткових ситуацій*** (exception handling) або ***обробка винятків*** — механізм мов програмування, призначений для опису реакції 
програми на помилки часу виконання та інші можливі проблеми
(винятки), які можуть виникнути при виконанні програми і призводять до 
неможливості (або ж безглуздості) подальшого відпрацювання програмою її базового 
алгоритма. 

## Обробка винятків в Python

Для обробки виняткових ситуацій в Python використовують спеціальну конструкцію: 

```python
try:
	# область дії обробника
except Exception1: 
	# обробник винятка Exception1
except (Exception2, Exception3):
	# обробник винятків Exception2 і Exception3
except Exception4 as exception: 
	# обробник винятка Exception4
	# екземпляр винятка доступний під іменем exception
except:
	# стандартний обробник, перехоплює усі винятки
```

Блок `try` задає область дії обробника винятків. 
Якщо при виконанні інструкцій в даному блоці було піднято виняток, 
їх виконання переривається 
і керування переходить до одного з обробників. 
Якщо не виникло жодного винятка, блоки `except` пропускаються. 

	>>> try:
	...     x = 2 / 0
	... except ZeroDivisionError:
	...     print('Division by zero detected')
	...
	Division by zero detected
	>>>

Після `except` можна вказати клас винятка, 
який ми плануємо перехопити, 
або ж одразу декілька класів, 
об'єднавши їх у кортеж. 

При перехопленні винятка створюється екземпляр відповідного класа, 
і ми маємо можливість отримати його: 

	>>> try:
	...     1/0
	... except Exception as e:
	...     print('oops!', e)
	...     catched = e
	...
	oops! division by zero
	>>> catched
	ZeroDivisionError('division by zero',)
	>>>
	
Якщо ж після `except` нічого не вказати, 
то будуть перехоплені усі винятки які ми не перехопили раніше. 
Бажано уникати такого перехоплення винятків, треба перехоплювати конкретні винятки. 

Блоки `except` обробляються від гори до низу і керування передається не більше, ніж одному обробнику. 
Тому при необхідності по-різному обробляти винятки, 
які знаходяться в ієрархії успадкування, 
спочатку треба вказувати обробники меньш загальних винятків, 
а потім — більш загальних. 
Саме тому стандартний блок `except` може бути тільки останнім. 

Приклад. У наступному коді ми ніколи не перехопимо ділення на нуль:

	>>> try:
	...     1/0
	... except Exception:
	...     print('Some exception catched')
	... except ZeroDivisionError:
	...     print('Zero division catched')
	...
	Some exception catched
	>>>

Якщо жоден з заданих блоків `except` не перехопив виняток, 
то його буде перехоплено найближчим зовнішнім блоком `try/except`, 
у якому є відповідний обробник. 
Якщо ж програма зовсім не перехопила виняток, 
то інтерпретатор завершує виконання програми і виводить 
інформацію про виняткову ситуацію в стандартний потік помилок `sys.stderr`. 

	>>> try:
	...     raise ValueError
	... except ZeroDivisionError:
	...     print('Division by zero')
	...
	Traceback (most recent call last):
	  File "<stdin>", line 2, in <module>
	ValueError
	>>>

Але у цього правила є винятки: 
якщо виняток виник в деструкторі об'єкта, 
виконання програми не завершується, 
а в стандартний потік помилок виводиться попередження `"Exception ignored"` з інформацією про сам виняток. 
	
Приклад. Наступний код:
	
```python
class MyClass(object):
	def __del__(self):
		raise ZeroDivisionError


print('Creating object')
obj = MyClass()

print('Deleting object')
del obj

print('Done')
```
дасть наступний результат:

	Creating object
	Deleting object
	Exception ignored in: <bound method MyClass.__del__ of <__main__.MyClass object at 0x000001AD476A97F0>>
	Traceback (most recent call last):
	  File "d:\PythonEssential2019\exception_in_destructor.py", line 3, in __del__
		raise ZeroDivisionError
	ZeroDivisionError:
	Done
	>>>

## Передача винятка на один рівень вгору

Для того, щоб в обробнику винятка виконати певні дії, 
а потім передати виняток далі, 
на один рівень обробників вище (тобто, викинути той самий виняток ще раз), 
використовується  інструкція `raise` без параметрів: 

	>>> try:
	...     1/0
	... except ZeroDivisionError:
	...     print('начебто обробили помилку')
	...     raise
	...
	начебто обробили помилку
	Traceback (most recent call last):
	File "<stdin>", line 2, in <module>
	ZeroDivisionError: division by zero
	>>>

## Блок else

В іннструкції `try` може бути присутнім необов'язковий блок `else`. 
Оператори всередині нього виконуються, якщо не виникло жодного винятка.

Приклад:

```python
def div10(x):
    try:
        result = 10 / x
    except ZeroDivisionError:
        return float('inf')
    else:
        return result
```

У цьому прикладі функція намагається поділити 10 на передане їй число. 
Якщо відбувається ділення на нуль, відповідний виняток обробляється в блоці `except`. 
Інакше виконується блок `else`, і функція повертає результат ділення.

	>>> div10(2)
	5.0
	>>> div10(0)
	inf
	>>>

## Блок finally

Також в іннструкції `try` може бути присутнім необов'язковий блок `finally`. 
Оператори всередині блока `finally` виконуються незалежно від того, чи виникла виняткова ситуація чи ні. 

	>>> try:
	...     2 / 0
	... finally:
	...     print('Finally block is always executed')
	...
	Finally block is always executed
	Traceback (most recent call last):
	  File "<stdin>", line 2, in <module>
	ZeroDivisionError: division by zero
	>>>

Блок `finally` виконується перед виходом з інструкції `try/except` завжди, 
навіть якщо одне з його відгалужень містить оператор `return` (коли оператор `try/except` знаходиться всередині функції), `break` чи `continue` (коли оператор `try/except` знаходиться всередині цикла) або ж виник інший необроблений виняток при обробці даного винятка.

```python
def div10(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return float('inf')
    finally:
        print('Це повідомлення виводиться завжди!')
```

Переконаємось:

	>>> div10(2)
	Це повідомлення виводиться завжди!
	5.0
	>>> div10(0)
	Це повідомлення виводиться завжди!
	inf
	>>>


Блок `finally` часто використовується для виконання так званих "дій по очистці" (cleanup actions), 
тобто дій, направлених на звільнення ресурсів: 
закриття файлів, видалення тимчасових об'єктів, тощо. 
