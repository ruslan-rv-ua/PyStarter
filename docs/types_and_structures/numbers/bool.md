---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Булевий тип даних

Має усього два значення: `False` та `True`. 

Тип `bool` успадковано від `int`: 

    >>> bool.mro()
    [<class 'bool'>, <class 'int'>, <class 'object'>]
    >>>
	
Успадковуватись від `bool` не можна: 

    >>> class A(bool):pass
    ...
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: type 'bool' is not an acceptable base type
    >>>

Літералам `False` та `True` відповідають цілі числа `0` і `1`. 

    >>> True == 1
    True
    >>> True is 1
    <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
    False
    >>> True * 7
    7
    >>>

### Створення об'єктів

- за допомогою літералів
- bool() без аргументів повертає `False`

### Приведення інших типів до `bool`

    bool(x)

Функція повертає `False` у наступних випадках: 

- якщо у об'єкта `x` визначено метод `__bool__()` і він повертає `False`
- якщо у об'єкта `x` визначено метод `__len__()` і він повертає `0`
- якщо значення `x` числового типу дорівнює нулю (0, 0.0, 0j, ...)
- якщо об'єкт `x` — пустий контейнер (list, str, tuple, dict, ...)
- якщо значення об'єкта `x` — одне з `None` чи `False`

У всіх інших випадках результатом функції буде `True`.

    >> bool(0)
    False
    >>> bool(1)
    True
    >>> bool('string')
    True
    >>> bool('')
    False
    >>> bool()
    False
    >>>


### Булевий контекст

Значення об'єктів можна розглядати як 
істиноподібні (truthy) і хибоподібні (falsy). 

- `x` є falsy, якщо `bool(x)==False`
- `x` є truthy, якщо `bool(x)==True`

Коли ми використовуємо значення у логічних виразах 
або при перевірці умов в інструкціях `if` та `while`, 
ми використовуємо їх у ***булевому контексті***. 

Приклад. Функції передається непустий список цілих чисел. 
Функція виводить лише парні числа з цього списка. 

```python
def print_even(data):
    if not data: # if len(data) == 0:
        raise ValueError("The argument data cannot be empty")
    for value in data:
        if not value % 2: # if value % 2 == 0:
            print(value)
```
Класи можуть визначати власний метод `__bool__()` для визначення поведінки екземплярів у булевому контексті:

    >>> class MyClass:          f):
    ...     def __bool__(self):
    ...         return False
    ...
    >>> c = MyClass()
    >>> bool(c)
    False
    >>> class AlwaysTrue: pass
    ...
    >>> c = AlwaysTrue()
    >>> bool(c)
    True
    >>>


### Логічні операції

Оператори у порядку збільшення пріорітету: 

|Операція|Результат|
|-|-|
|`x or y`|`y` якщо `bool(x) is False`, інакше `x`|
|`x and y`|`x` якщо `bool(x) is False`, інакше `y`|
|`not x`|`True` якщо `bool(x) is False`, інакше `False`|

Приклади: 

    >>> 7 or 5
    7
    >>> 'string' or None
    'string'
    >>> None or 'string'
    'string'
    >>> def f(list_=None): # аргумент з дефолтним значенням [] мутабельного типу — не найкраща ідея, тому None
    ...     new_list = list_ or []
    ...     return new_list
    ...
    >>> f()
    []
    >>> f([1,2])
    [1, 2]
    >>>
    >>> 7 and 5
    5
    >>> 'string' and False
    False
    >>> False and 'string'
    False
    >>>

Оператор `not` має нижчий пріорітет ніж інші "нелогічні" оператори. 
Тому вираз 

    not a == b
    
інтерпретується як

    not (a == b)
    
Наступний вираз: 

    a == not b
    
не є коректним і призведе до `SyntaxError`. 

### "Ліниві" логічні обчислення

Операція `or` є "лінивою". 
Значення другого операнда обчислюється лише тоді, коли перший операнд є falsy: 

    >>> l = [1, 2]
    >>> l.pop() or l.pop()
    2
    >>> l
    [1]
    >>> l = [1, 0]
    >>> l.pop() or l.pop()
    1
    >>> l
    []
    >>>

Операція `and` є "лінивою". 
Значення другого операнда обчислюється лише тоді, коли перший операнд є truthy: 

    >>> l = [1, 0]
    >>> l.pop() and l.pop()
    0
    >>> l
    [1]
    >>> l = [1, 2]
    >>> l.pop() and l.pop()
    1
    >>> l
    []
    >>>

### Операції порівняння

Усього в Python є вісім операцій порівняння. 
Усі операції порівняння мають однаковий пріорітет. 
У операцій порівняння пріорітет вищий ніж у логічних операцій. 

|Операція|Що означає|Спеціальний метод|
|-|-|-|
|<|строго меньше|`__lt__()`|
|<=|меньше або дорівнює|`__le__()`|
|>|строго більше|`__gt__()`|
|>=|більше або дорівнює|`__ge__()`|
|==|дорівнює|`__eq__()`|
|!=|не дорівнює|`__ne__()`|
|is|ідентичне||
|is not|неідентичне||

#### Згортання операцій порівняння

Наступний вираз:

    x < y <= z

є еквівалентом виразу:

    x < y and y <= z
    
Зауважте: значення `y` обчислюється лише один раз.

Приклад:

```python
def f(val):
    print(f"f({val}) called")
    return val
```

Використання функції `f` у виразі `x < y <= z`:

```python
>>> f(1) < f(2) <= f(3)
f(1) called
f(2) called
f(3) called
True
>>>
```

Порівняйте з:

```python
>>> f(1) < f(2) and f(2) <= f(3)
f(1) called
f(2) called
f(2) called
f(3) called
True
>>>
```

#### Оператори ідентичності `is` та `is not`

Поведінка `is` та `is not` не може бути перевизначена. 
Ця операція працює з об'єктами будь-яких класів і ніколи не піднімає винятків. 

    >>> a=1
    >>> s='s'
    >>> a is s
    False
    >>>

#### Оператори порівняння значень

Об'єкти різних типів, за винятком числових, при порівнянні на рівність завжди дають `False`. 

    >>> [1,2] == '12'
    False
    >>> 1 == 1.0
    True
    >>> 1 == True
    True
    >>> [] == ()
    False
    >>>

Об'єкти одного класа за замовчуванням не рівні між собою — оператор `==` для об'єктів поводиться так само, як оператор `is`:

    >>> class MyClass:
    ...     def __init__(self, value):
    ...             self.value = value
    ...
    >>> c1 = MyClass(1)
    >>> c2 = MyClass(1)
    >>> c1 == c2
    False
    >>> c1 is c2
    False
    >>>

##### `__eq__`

Цей метод викликається, коли використовується оператор `==`. 

Повинен повернути:

- `True`, якщо об'єкти рівні.
- `False`, якщо об'єкти не рівні.
- `NotImplemented`, якщо об'єкти несумісні для порівняння.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            # Не порівнювати з об'єктами інших типів
            return NotImplemented
        return self.name == other.name and self.age == other.age

p1 = Person("Іван", 30)
p2 = Person("Марія", 25)
p3 = Person("Іван", 30)
```

Порівнюємо два об'єкти `Person`:

```python
>>> p1 == p2
False
>>> p1 == p3
True
>>> p1 == "Іван" # завдяки NotImplemented
False
>>>
```

Якщо `__eq__` реалізований, а `__ne__` ні,
то `__ne__` за замовчуванням повертає протилежне значення `__eq__`.

```python
>>> p1 != p2
True
>>> p1 != p3
False
>>>
```

Якщо `__eq__` не реалізований, він успадковується від класу `object`, який у свою чергу повертає `NotImplemented`.
У цьому разі Python за замовчуванням порівнює ідентифікатори об'єктів (тобто, чи є це один і той же об'єкт в пам'яті).

##### `__ne__`

Метод викликається для оператора `!=`. 

Зазвичай, якщо реалізували `__eq__`, вам не потрібно явно реалізовувати `__ne__`, 
оскільки Python автоматично надасть реалізацію за замовчуванням, 
яка є запереченням `__eq__`. 
Однак, ви можете надати власну реалізацію, якщо це необхідно.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # Явна реалізація __ne__ (хоча зазвичай не потрібна)
    def __ne__(self, other):
        print("Викликано __ne__")
        if not isinstance(other, Point):
            return NotImplemented
        return not self.__eq__(other)


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
```

Порівнюємо два об'єкти `Point`:

```python
>>> p1 != p3
Викликано __ne__
True
>>> p1 != p2
Викликано __ne__
False
>>>
```

##### Методи впорядкованого порівняння: `__lt__`, `__le__`, `__gt__`, `__ge__`

Ці методи використовуються для операторів `<`, `<=`, `>`, `>=` відповідно. 

Метод ``__lt__(self, other)` повинен повернути:

- `True`, якщо `self` менше `other`.
- `False`, якщо `self` не менше `other`.
- `NotImplemented`, якщо `self` і `other` несумісні для порівняння.

Аналогічно для інших методів.

Приклад з `__lt__`:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price and self.name == other.name

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

laptop = Product("Ноутбук", 1500)
keyboard = Product("Клавіатура", 30)
```

Порівнюємо два об'єкти `Product`:

```python
>>> keyboard < laptop
True
>>> laptop < keyboard
False
>>>
```

##### `NotImplemented`

Спеціальне значення `NotImplemented` використовується в методах порівняння, щоб вказати, що операція не реалізована для наданого типу `other`. Якщо метод порівняння повертає `NotImplemented`, Python спробує викликати "віддзеркалений" метод на іншому операнді. Якщо обидва повертають `NotImplemented`, виникає `TypeError`.

Ось як працюють віддзеркалені методи:

*   `__lt__(self, other)` та `__gt__(self, other)` є взаємними віддзеркаленнями. Тобто, якщо `a.__lt__(b)` повертає `NotImplemented`, Python спробує `b.__gt__(a)`.
*   `__le__(self, other)` та `__ge__(self, other)` є взаємними віддзеркаленнями. Якщо `a.__le__(b)` повертає `NotImplemented`, Python спробує `b.__ge__(a)`.
*   `__eq__(self, other)` та `__ne__(self, other)` є віддзеркаленнями самі для себе. Якщо `a.__eq__(b)` повертає `NotImplemented`, Python спробує `b.__eq__(a)`.

Приклад віддзеркалених методів:

```python
class A:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        print("A.__lt__ викликано")
        if isinstance(other, B):
            # A не знає, як порівнюватися з B напряму для <
            return NotImplemented
        if isinstance(other, A):
            return self.value < other.value
        return NotImplemented # Для інших невідомих типів

class B:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        print("B.__gt__ викликано")
        if isinstance(other, A):
            # B знає, як порівнюватися з A, коли B > A (що еквівалентно A < B)
            return self.value > other.value
        if isinstance(other, B):
            return self.value > other.value
        return NotImplemented # Для інших невідомих типів

a1 = A(5)
a2 = A(10)
b1 = B(7)
```

1. Буде викликано `A.__lt__`.

```python
>>> a1 < a2
A.__lt__ викликано
True
>>>
```

2. Спочатку викликається `A.__lt__(a1, b1)`, який поверне `NotImplemented`. 
Потім Python спробує `B.__gt__(b1, a1)`.

```python
>>> a1 < b1
A.__lt__ викликано
B.__gt__ викликано
True
>>>
```

Якби `B.__gt__` також повернув `NotImplemented` або не був визначений, 
виникла б помилка `TypeError`.

Коли операнди (`a` та `b` в `a < b`) належать до різних типів, Python дотримується певних правил для визначення, який метод викликати першим:

1.  **Загальний випадок:** Зазвичай Python спочатку викликає метод лівого операнда (наприклад, `a.__lt__(b)`). Якщо він повертає `NotImplemented`, тоді викликається віддзеркалений метод правого операнда (наприклад, `b.__gt__(a)`).
2.  **Пріоритет підкласу:** Якщо тип правого операнда є прямим або непрямим підкласом типу лівого операнда, то **віддзеркалений метод правого операнда має пріоритет**. Наприклад, в операції `a < b`, якщо `type(b)` є підкласом `type(a)`, Python спочатку спробує `b.__gt__(a)`. Лише якщо цей виклик поверне `NotImplemented`, Python спробує `a.__lt__(b)`.
<!-- 3.  **Віртуальне успадкування:** Ці правила пріоритету базуються на фактичній ієрархії класів і не враховують віртуальне успадкування (наприклад, через `ABCMeta.register`). -->

Це дозволяє об'єктам різних типів коректно взаємодіяти, особливо коли один з них (наприклад, підклас) має більш специфічну логіку порівняння.

##### Рекомендації

- Повертайте `NotImplemented` при порівнянні з несумісними типами, замість того, щоб викликати `TypeError` напряму.
- Будьте послідовними. Логіка порівняння повинна бути інтуїтивно зрозумілою та відповідати очікуванням. Наприклад, якщо `a == b` і `b == c`, то `a == c` повинно бути істинним.
