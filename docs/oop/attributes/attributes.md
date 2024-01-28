---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Атрибути: як це працює

<!--https://realpython.com/python-classes/#instance-attributes -->

До атрибутів певного об'єкта чи класа можна дістатись використовуючи "крапкову нотацію", 
тобто вказуючи об'єкт або клас і через крапку ім'я атрибута. 
Але це не єдиний спосіб отримати доступ до атрибутів. 

Подивимось як це можна зробити з наступним класом та його екземпляром: 

```python
class Person:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        print(f'I am {self.name}')

p = Person('Jane')
```

### `getattr()`

Вбудована функція. Дозволяє отримати значення атрибута по імені. 

```python
getattr(target_object, attr_name, default_value)
```

**Параметри:**

- `target_object` — об'єкт, значення атрибута якого треба отримати.
- `attr_name` — символьний рядок, ім'я атрибута значення якого треба отримати.
- `default_value` — необов'язковий, значення яке буде повернуто в разі відсутності атрибута зі вказаним ім'ям.

**Повертає:**

- значення атрибута зі вказаним іменем якщо такий існує
- задане значення за замовчуванням якщо атрибут зі вказаним іменем у об'єкта відсутній
- в інших випадках — помилка `AttributeError`.

**Приклад використання:**

    >>> getattr(p, 'name')
    'Jane'
    >>> getattr(p, 'age', 24)
    24
    >>> getattr(p, 'age')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'Person' object has no attribute 'age'
    >>> getattr(Person, 'species')
    'Homo sapiens'
    >>>

### `setattr()`

Функція `setattr()` використовується для встановлення значення атрибута об'єкта за іменем. 

```python
setattr(target_object, attr_name, new_value)
```

**Параметри:**

- `target_object` — об'єкт, для якого ми хочемо змінити атрибут.
- `attr_name` — символьний рядок, ім'я атрибута, значення якого ми хочемо змінити.
- `new_value` — нове значення, яке буде встановлено для вказаного атрибута.

**Приклад використання:**

    >>> setattr(p, 'name', 'Alice')
    >>> p.name
    'Alice'
    >>> setattr(p, 'email', 'alice@wonderland.nowhere')
    >>> p.email
    'alice@wonderland.nowhere'
    >>> Person.species
    'Homo neanderthalensis'
    >>> p.species
    'Homo neanderthalensis'
    >>>

### `delattr()`

Функція `delattr()` дозволяє видаляти атрибути об'єкта за їхнім іменем. 

```python
delattr(target_object, attr_name)
```

**Параметри:**

- `target_object` — об'єкт, для якого ми хочемо видалити атрибут.
- `attr_name` — символьний рядок, ім'я атрибута, який ми хочемо видалити.

**Приклад використання:**

    >>> delattr(p, 'name')
    >>> getattr(p, 'name', 'N/A')
    'N/A'
    >>> delattr(p, 'phone')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'Person' object has no attribute 'phone'
    >>>


### `hasattr()`

Функція `hasattr()` служить для перевірки наявності атрибута у об'єкта за його іменем. 


```python
hasattr(target_object, attr_name)
```

**Параметри:**

- `target_object` — об'єкт, для якого ми перевіряємо наявність атрибута.
- `attr_name` — символьний рядок, ім'я атрибута, наявність якого ми перевіряємо.

**Повертає:**

- логічне значення `True`, якщо атрибут існує, і `False` в іншому випадку.

**Приклад використання:**

    >>> p = Person('Jane')
    >>> hasattr(p, 'name')
    True
    >>> hasattr(p, 'address')
    False
    >>> hasattr(Person, 'species')
    True
    >>>

Функція `hasattr()` може бути корисною, коли потрібно перевірити, чи існує певний атрибут перед його використанням.






### Де "ховаються" атрибути

В Python у кожного об'єкта є спеціальний атрибут `__dict__`. 
Цей атрибут вказує на словник, у якому і "зберігаються" усі атрибути об'єкта. 

```python
class Person:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        print(f'I am {self.name}')
```

Перевіримо атрибути екземпляра класа `Person`: 

    >>> p = Person('Jane')
    >>> p.__dict__
    {'name': 'Jane'}
    >>> p.__dict__['name']
    'Jane'
    >>>

Через цей словник цілком можна міняти значення атрибутів а також додавати нові атрибути: 

    >>> p.__dict__['name'] = 'Alice'
    >>> p.name
    'Alice'
    >>> p.__dict__['age'] = 24
    >>> p.age
    24
    >>>

Доступ до атрибута `__dict__` можна отримати також за допомогою вдудованої функції `vars()`: 

    >>> vars(p)
    {'name': 'Alice', 'age': 24}
    >>>

Пам'ятаючи, що в Python усе є об'єкт, і класи також, до атрибутів класа також можна отримати доступ через `__dict__`: 

    >>> Person.__dict__
    mappingproxy({'__module__': '__main__', 'species': 'Homo sapiens', '__init__': <function Person.__init__ at 0x0000016A634CC9A0>, 'say_hello': <function Person.say_hello at 0x0000016A634F8040>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None})
    >>>

Як бачимо це об'єкт класа `mappingproxy`, тобто спеціальний об'єкт-посередник. 
Отримати атрибути класа можна з такого об'єкта як і у словника — по ключу. 
Але змінити значення атрибута класа вже не вийде: 

    >>> Person.__dict__['species']
    'Homo sapiens'
    >>> Person.__dict__['species'] = 'Homo neanderthalensis'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'mappingproxy' object does not support item assignment
    >>>

Атрибут `__dict__` слід використовувати лише у певних особливих випадках, коли доступ до атрибутів "звичайними" методами неможливий. 
