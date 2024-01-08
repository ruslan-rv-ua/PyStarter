---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Представлення екземпляра класа

Часто буває корисним представлення екземпляра класа у вигляді символьного рядка. 
В Python для цього є дві функції: `repr()` та `str()`. 
Головна відмінність `repr()` від `str()` — в цільовій аудиторії. 
`repr()` більше призначено для машино-орієнтованого вивода, 
більш того, це по можливості має бути валідний код на Python для створення екземпляра класа. 
`str()` призначено для читання людьми. 

	>>> str('text')
	'text'
	>>> repr('text')
	"'text'"
	>>> print(str('test'))
	test
	>>> print(repr('test'))
	'test'
	>>>

В Python кожен клас має спеціальні методи, 
які ви можете перевизначити для налаштування поведінки вбудованих функцій при представленні вашого класа. 

* `__str__()` — 
визначає поведінку функції `str()`, яка була викликана для екземпляра вашого класа.

* `__repr__()` — 
визначає поведінку вбудованої функції `repr()`, викликаної для екземпляра вашого класа. 

Створимо клас і визначимо представлення екземпляра:

	class Person:
		def __init__(self, name, email):
			self.name = name
			self.email = email
		def __str__(self):
			return f'{self.name} <{self.email}>'
		def __repr__(self):
			return f'Person(name={repr(self.name)}, email={repr(self.email)})'

Створимо екземпляр класа і подивимось як він тепер "виглядає":
			
	>>> p = Person('Alice', 'alice@wonderland.org')
	>>> repr(p)
	"Person(name='Alice', email='alice@wonderland.org')"
	>>> p
	Person(name='Alice', email='alice@wonderland.org')
	>>> str(p)
	'Alice <alice@wonderland.org>'
	>>> print(p)
	Alice <alice@wonderland.org>
	>>>
