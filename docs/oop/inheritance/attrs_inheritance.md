---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Успадкування атрибутів класа

Дочірній клас успадковує атрибути базового класа. 

Розглянемо на прикладі: 

```python
class Person:
    def __init__(self, name):
        print('Виклик ініціалізатора класа Person')
        self.name = name
    def person_method(self):
        print('Це метод з класа Person')
        print(f'У екземпляра класа Person є атрибут {self.name=}')

class Employee(Person):
	def employee_method(self):
		print('Це метод з класа Employee')
		print(f'У екземпляра класа Employee є атрибут {self.name=}')
```

Подивимось що тут відбувається: 

1. Клас `Employee` не має власного ініціалізатора, отже він успадкує його від класа `Person`
1. При створенні екземпляра класа `Employee` буде викликано успадкований ініціалізатор
1. В ініціалізаторі для екземпляра буде створено атрибут `name`
1. Клас `Employee` успадкує від класа `Person` метод `person_method()`
1. Клас `Employee` має свій власний метод: `employee_method()`

Перевіримо на практиці: 

	>>> e = Employee('Bob')
	Виклик ініціалізатора класа Person
	>>> e.person_method()
	Це метод з класа Person
	У екземпляра класа Person є атрибут self.name='Bob'
	>>> e.employee_method()
	Це метод з класа Employee
	У екземпляра класа Employee є атрибут self.name='Bob'
	>>> e.name
	'Bob'
	>>>

## Успадкування і приватні атрибути

Як нам вже відомо, 
атрибути, які починаються з двох символів підкреслення (але не закінчуються ними) 
є приватними атрибутами класа. 
Поза видимістю класа до таких атрибутів застосовується механізм `name mangling` (спотворення імені), 
тобто такі атрибути "поза класом" будуть мати інші імена (клас+атрибут), 
у тому числі і в успадкованих класах. 

Використання приватних атрибутів дозволяє "приховати" внутрішню реалізацію базового класа 
для дочірніх класів. 
Тобто у дочірньому класі приватні атрибути базового класа не успадковуються: 

```python
class Person:
    def __init__(self, name):
        print('Виклик ініціалізатора класа Person')
        self.__name = name
    def person_method(self):
        print('Це метод з класа Person')
        print(f'У екземпляра класа Person є атрибут {self.__name=}')

class Employee(Person):
    def employee_method(self):
        print('Це метод з класа Employee')
        print(f'У екземпляра класа Employee є атрибут {self.__name=}')
```

Перевіримо:

	>>> e = Employee('Bob')
	Виклик ініціалізатора класа Person
	>>> e.person_method()
	Це метод з класа Person
	У екземпляра класа Person є атрибут self.__name='Bob'
	>>> e.employee_method()
	Це метод з класа Employee
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "e:\dev\PyStarter\docs\oop\inheritance\demo\2e_attrs_inheritance.py", line 39, in employee_method
		print(f'У екземпляра класа Employee є атрибут {self.__name=}')
													^^^^^^^^^^^
	AttributeError: 'Employee' object has no attribute '_Employee__name'
	>>>

З метода `person_method()` "видно" атрибут `__name` тому що вони знаходяться в одному класі `Person`. 
"Розгорнуте" ім'я атрибута буде `_Person__name`. 

Якщо ж ми звертаємось до атрибута `__name` у методі `employee_method()`, 
то тоді "розгорнуте" ім'я такого атрибута буде `_Employee__name`. 
А клас `Employee` не має свого власного приватного атрибута `__name`. 
