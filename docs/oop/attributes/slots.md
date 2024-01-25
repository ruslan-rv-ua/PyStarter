---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Слоти

Слоти — це механізм в мові програмування Python, який дозволяє заздалегідь визначити структуру атрибутів об'єкта і вказати, які саме атрибути можуть бути створені для екземплярів класу. 

При створенні класа у спеціальлному атрибуті `__slots__` вказуємо ідентифікатори атрибутів: 

```python
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

У екземплярів такого класа просто відсутній спеціальний атрибут `__dict__`: 

    >>> p = Point(42, 24)
    >>> p.x
    42
    >>> p.__dict__
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'Point' object has no attribute '__dict__'. Did you mean: '__dir__'?
    >>>

Відповідно створювати нові атрибути ми теж не зможемо: 

    >>> p.z = 3
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'Point' object has no attribute 'z'
    >>>

Динамічний словник `__dict__` замінюється фіксованим набором атрибутів, що дозволяє заощаджувати пам'ять та підвищити продуктивність. 


### Слоти і спадковість

Атрибут `__slots__` успадковується. 

```python
class Point:
    __slots__ = ('x', 'y')

class Point3D(Point):
    pass
```

Але це не перешкоджає створенню `__dict__` у екземплярах похідного класа 
з усіма відповідними витратами по пам'яті та продуктивності. 
Також ми знову можемо створювати атрибути динамічно: 

    >>> p.__slots__
    ('x', 'y')
    >>> p.extra = 'oops'
    >>> p.__dict__
    {'z': 5, 'extra': 'oops'}
    >>>

Але у похідному класі ми теж можемо визначити `__slots__`. 
При цьому дублювати слоти з базового класа вже не треба. 

```python
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point):
    __slots__ = ('z',)

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
```

Множинне успадкування можливе якщо лише один з базових класів визначає `__slots__`. 

    >>> class B1:
    ...     __slots__ = 'b1'
    ...
    >>> class B2:
    ...     __slots__ = 'b2'
    ...
    >>> class C(B1, B2):
    ...     pass
    ...
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: multiple bases have instance lay-out conflict
    >>>

### Практики використання

Переваги використання слотів:

- економія пам'яті
- запобігання динамічному додаванню атрибутів
- покращення швидкодії
- зменшення ймовірності одруків

При використанні слотів важливо добре обмірковувати структуру класів і їх відносини, оскільки вони можуть вплинути на спадковість та доступ до атрибутів.

<!-- https://habr.com/ru/articles/686220/ -->