---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Успадкування в Python

В Python синтаксис для наслідування класів виглядає наступним чином: 
при створенні класа після його імені в круглих дужках можна вказати імена одного або декількох суперкласів. 

```python
class Base:
	pass

class Child(Base):
	pass
```
		
У вищенаведеному коді: 

- `Child` — це дочірній (похідний) клас, підклас
- `Base` — це базовий (батьківський) клас, суперклас

В Python є вбудований клас який має назву `object`. 
Від цього класа явно чи неявно успадковуються усі інші класи, 
як вбудовані, так і ті, що створююте ви. 
Якщо при створенні класа ви не вказуєте базовий клас, 
то неявним чином ваш клас буде успадковано від `object`. 
Отже наступні оголошення класа рівносильні: 

```python
class Base:
	pass
	
class Base():
	pass
	
class Base(object):
	pass
```		
		
## Ієрархія успадкування

Клас може бути успадкованим від класа, 
який у свою чергу було успадковано від іншого класа. 
Коли розглядають увесь ланцюжок успадкованих і базових класів, 
говорять про **ієрархію успадкування**. 

Розглянемо наступну ієрархію класів: 

```python
class Person:
	pass

class Employee(Person):
	pass

class Manager(Employee):
	pass
```	

У вищенаведеному прикладі: 

- клас `Person` успадковано від `object`
- клас `Employee` успадковано від `Person`
- клас `Manager` успадковано від `Employee`

Дізнатись, чи є певний клас підкласом іншого класа по всій ієрархії успадкування, 
можна за допомогою вбудованої функції: 

	issubclass(cls, super_class)
	 
Функція повертає `True` якщо `cls` є дочірнім класом `super_class` або ж є тим самим класом. 

Розвиваючи вищенаведений приклад: 

	>>> issubclass(Manager, Employee)
	True
	>>> issubclass(Manager, Person)
	True
	>>> issubclass(Manager, object)
	True
	>>> issubclass(Manager, Manager)
	True
	>>>
	>>> issubclass(Employee, Manager)
	False
	>>> issubclass(Employee, Person)
	True
	>>> issubclass(Person, Employee)
	False
	>>> issubclass(str, object)
	True
	>>>

Функції `issubclass` другим аргументом можна передати одразу декілька класів об'єднаних у кортеж. 
У такому разі функція поверне `True` якщо вказаний клас є дочірнім хоча б одному з перерахованих: 

	>>> issubclass(Manager, (Person,Employee))
	True
	>>> issubclass(Manager, (Employee,object))
	True
	>>> issubclass(Employee, (object, Manager))
	True
	>>> issubclass(Person, (Employee, Manager))
	False
	>>>
	>>>

А тепер вкотре згадаємо що "в Python усе є об'єкт". 
І класи тут теж не виключення, тобто класи — це теж об'єкти. 
І як об'єкти вони мають свої атрибути. 

У кожного класа є спеціальний атрибут `__bases__`, 
у якому міститься базовий клас, точніше кортеж який містить усі базові класи 
(чому їх може бути декілька — дізнаємось у подальшому): 

	>>> Manager.__bases__
	(<class '__main__.Employee'>,)
	>>> Person.__bases__
	(<class 'object'>,)
	>>>
