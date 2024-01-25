# Обробка винятків

> ***Обробка виняткових ситуацій*** (exception handling) або ***обрабка винятків*** — механізм мов програмування, призначений для опису реакції 
програми на помилки часу виконання та інші можливі проблеми
(винятки), які можуть виникнути при виконанні програми і призводять до 
неможливості (або ж безглуздості) подальшого відпрацювання програмою її базового 
алгоритма. 

## Обробка винятків в Python

Для обробки виняткових ситуацій в Python використовують спеціальну конструкцію: 

	:::python
	try:
		# область дії обробника
		pass
	except Exception1: 
		# обробник винятка Exception1
		pass
	except (Exception2, Exception3):
		# обробник винятків Exception2 і Exception3
		pass
	except Exception4 as exception: 
		# обробник винятка Exception4
		# екземпляр винятка доступний під іменем exception
		pass
	except:
		# стандартний обробник, перехоплює усі винятки
		pass

Блок `try` задає область дії обробника винятків. 
Якщо при виконанні інструкцій в даному блоці було піднято виняток, 
їх виконання переривається 
і керування переходить до одного з обробників. 
Якщо не виникло жодного винятка, блоки `except` пропускаються. 

	:::python
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

	:::python
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

	:::python
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

	:::python
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
	
	:::python
	class MyClass(object):
		def __del__(self):
			raise ZeroDivisionError


	print('Creating object')
	obj = MyClass()

	print('Deleting object')
	del obj

	print('Done')

дасть наступний результат:

	:::python
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

	:::python
	try:
		do_some_actions() # дії, які можуть призвести до винятка
	except Exception as exception: # обробник винятка
		handle_exception(exception) # певні дії з перехопленим винятком
		raise

## Блок else

В конструкції `try...except...` може бути присутнім необов'язковий блок `else`. 
Оператори всередині нього виконуються, якщо не виникло жодного винятка.

## Блок finally

Також  конструкції `try...except...` може бути присутнім необов'язковий блок `finally`. 
Оператори всередині блока `finally` виконуються незалежно від того, чи виникла виняткова ситуація чи ні. 

	:::python
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

Блок `finally` використовується для виконання так званих "дій по очистці" (cleanup actions), 
тобто дій, направлених на звільнення ресурсів: 
закриття файлів, видалення тимчасових об'єктів, тощо. 

Блок `finally` виконується перед виходом з оператора `try/except` завжди, 
навіть якщо одне з його відгалужень містить оператор `return` (коли оператор `try/except` знаходиться всередині функції), `break` чи `continue` (коли оператор `try/except` знаходиться всередині цикла) або ж виник інший необроблений виняток при обробці даного винятка.

	:::python
	>>> def f():
	...     try:
	...             2 / 0
	...     except Exception as e:
	...             return 'We have catched: ' + str(e)
	...     finally:
	...             print('Finally block is always executed')
	...
	>>> print(f())
	Finally block is always executed
	We have catched: division by zero
	>>>
