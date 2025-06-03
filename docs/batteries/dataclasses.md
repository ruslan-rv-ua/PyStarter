---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Датакласи

Модуль `dataclasses` надає декоратор та функції для автоматичного додавання спеціальних методів, таких як `__init__()`, `__repr__()`, `__eq__()` 
та інших, до класів, визначених користувачем. 
Це значно спрощує створення класів, які переважно використовуються для зберігання даних. Датакласи були вперше описані в [PEP 557](https://www.python.org/dev/peps/pep-0557/).

Датаклас – це звичайний клас Python, 
до якого автоматично додаються стандартні методи. 
Основна ідея полягає в тому, щоб зменшити кількість шаблонного коду, який розробники змушені писати.

Переваги:

*   **Менше коду**: Автоматична генерація методів `__init__`, `__repr__`, `__eq__` тощо.
*   **Читабельність**: Чітке визначення полів класу з їх типами.
*   **Підтримка типів**: Використання анотацій типів ([PEP 526](https://www.python.org/dev/peps/pep-0526/)) для визначення полів.
*   **Гнучкість**: Можливість налаштовувати поведінку генерованих методів.

Для створення датакласу достатньо задекорувати клас за допомогою `@dataclass`:

```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```

У цьому прикладі для класу `InventoryItem` будуть автоматично згенеровані, серед іншого, 
метод `__init__()`, який виглядатиме приблизно так:

```python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
```

### Автоматично генеровані методи

За замовчуванням `@dataclass` генерує наступні методи:

*   **`__init__(self, field1: type, field2: type, ...)`**: Ініціалізує екземпляр класу. Поля визначаються на основі анотацій типів.
*   **`__repr__(self)`**: Повертає рядкове представлення об'єкта, зручне для налагодження. Наприклад: `InventoryItem(name='widget', unit_price=3.0, quantity_on_hand=10)`.
*   **`__eq__(self, other)`**: Порівнює два екземпляри на рівність. Порівняння відбувається поелементно для всіх полів.
*   **`__lt__(self, other)`, `__le__(self, other)`, `__gt__(self, other)`, `__ge__(self, other)`**: Методи порівняння (менше, менше або дорівнює, більше, більше або дорівнює). Генеруються, якщо `order=True`. Порівняння відбувається поелементно, як у кортежів.
*   **`__hash__(self)`**: Генерується, якщо `eq=True` та `frozen=True` (або `unsafe_hash=True`).

### Параметри декоратора

Декоратор `@dataclass` приймає кілька необов'язкових параметрів для налаштування своєї поведінки:

*   **`init=True`**: Якщо `True` (за замовчуванням), генерується метод `__init__()`. Якщо `False`, метод `__init__()` не генерується (або використовується той, що вже визначений у класі).
*   **`repr=True`**: Якщо `True` (за замовчуванням), генерується метод `__repr__()`.
*   **`eq=True`**: Якщо `True` (за замовчуванням), генерується метод `__eq__()`.
*   **`order=False`**: Якщо `True`, генеруються методи `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`. Це призведе до того, що екземпляри можна буде сортувати. Якщо `order=True`, а `eq=False`, виникне `ValueError`.
*   **`unsafe_hash=False`**: Якщо `False` (за замовчуванням), метод `__hash__()` генерується відповідно до значень `eq` та `frozen`.
    *   Якщо `eq` та `frozen` обидва `True`, `__hash__()` генерується.
    *   Якщо `eq` є `True`, а `frozen` є `False`, `__hash__` встановлюється в `None`, позначаючи його як нехешований (що є поведінкою за замовчуванням для змінних класів).
    *   Якщо `eq` є `False`, `__hash__` залишається без змін (успадковується від базового класу, зазвичай `object.__hash__`).
    Якщо `unsafe_hash=True`, генерується метод `__hash__()` незалежно від налаштувань `eq` та `frozen`. Це небезпечно, якщо клас логічно незмінний, але може бути змінним.
*   **`frozen=False`**: Якщо `True`, присвоєння значень полям після створення екземпляра викликатиме виняток `FrozenInstanceError`. Це робить екземпляри датакласу фактично незмінними (immutable). Якщо `frozen=True`, датаклас генеруватиме метод `__hash__()`, якщо він ще не визначений.
*   **`match_args=True`** (Python 3.10+): Якщо `True` (за замовчуванням), атрибут `__match_args__` генерується зі списку імен полів, які включені в `__init__`. Це використовується для позиційного зіставлення за шаблоном (pattern matching).
*   **`kw_only=False`** (Python 3.10+): Якщо `True`, всі поля за замовчуванням позначаються як keyword-only (тобто, їх можна передати лише за ключовим словом при створенні екземпляра). Це можна перевизначити для окремих полів за допомогою `field(kw_only=False)`.
*   **`slots=False`** (Python 3.10+): Якщо `True`, генерується атрибут `__slots__` і клас не матиме `__dict__`. Це може зекономити пам'ять для класів з великою кількістю екземплярів.
*   **`weakref_slot=False`** (Python 3.11+): Якщо `True`, додає поле `__weakref__`, що дозволяє екземплярам бути ціллю слабких посилань. Це актуально, якщо `slots=True`.

Приклад використання параметрів:

```python
from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(0.5, 3.0)
```

Використовуємо:

```python
>>> p1 == p2
False
>>> p1 > p2 # порівнює спочатку x, потім y
True
>>> p1.x = 5.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 4, in __setattr__
dataclasses.FrozenInstanceError: cannot assign to field 'x'
>>>
```

### Функція `field()` для детального налаштування полів

Функція `field()` використовується для налаштування кожного поля окремо. Вона приймає наступні параметри:

*   **`default=MISSING`**: Якщо надано, це буде значенням за замовчуванням для поля. `MISSING` – це спеціальний об'єкт-маркер, який вказує на відсутність значення.
*   **`default_factory=MISSING`**: Функція без аргументів, яка викликається для створення початкового значення поля. Це корисно для змінних типів даних (наприклад, `list` або `dict`), щоб уникнути спільного використання одного об'єкта між різними екземплярами класу. Не можна одночасно вказувати `default` та `default_factory`.
    ```python
    from dataclasses import dataclass, field
    from typing import List

    @dataclass
    class C:
        mylist: List[int] = field(default_factory=list)

    c1 = C()
    c1.mylist.append(1)
    c2 = C()
    print(c2.mylist)  # Виведе: [] (а не [1])
    ```
*   **`init=True`**: Якщо `True` (за замовчуванням), це поле включається як параметр до генерованого методу `__init__()`.
*   **`repr=True`**: Якщо `True` (за замовчуванням), це поле включається до рядка, що генерується методом `__repr__()`.
*   **`hash=None`**: Може бути `True`, `False` або `None` (за замовчуванням). Якщо `True`, це поле включається до генерованого методу `__hash__()`. Якщо `False`, поле виключається. Якщо `None`, використовується значення `compare`.
*   **`compare=True`**: Якщо `True` (за замовчуванням), це поле включається до генерованих методів порівняння (`__eq__()`, `__gt__()` тощо).
*   **`metadata=None`**: Словник або `None`. Якщо надано, зберігається як `MappingProxyType` і може використовуватися сторонніми бібліотеками.
*   **`kw_only=MISSING`** (Python 3.10+): Якщо `True`, це поле буде keyword-only. Якщо `False`, воно буде позиційним. За замовчуванням (`MISSING`) використовується значення `kw_only` з декоратора `@dataclass`.

Приклад використання `field()`:

```python
from dataclasses import dataclass, field
import uuid

@dataclass
class Book:
    title: str
    author: str
    isbn: str = field(repr=False, compare=False) # Не показувати в repr, не використовувати для порівняння
    book_id: uuid.UUID = field(default_factory=uuid.uuid4, init=False) # Генерується автоматично, не в __init__

book1 = Book("The Hobbit", "J.R.R. Tolkien", "12345")
book2 = Book("The Hobbit", "J.R.R. Tolkien", "67890")

print(book1)        # Виведе: Book(title='The Hobbit', author='J.R.R. Tolkien')
print(book1 == book2) # Виведе: True (isbn не порівнюється)
print(book1.book_id)  # Виведе унікальний UUID
```

### Пост-ініціалізаційна обробка

Якщо в датакласі визначено метод `__post_init__()`, 
він автоматично викликається згенерованим `__init__()` після ініціалізації всіх полів. 
Це дозволяє виконувати додаткову валідацію або обчислення на основі переданих значень.

```python
from dataclasses import dataclass, field

@dataclass
class Rectangle:
    height: float
    width: float
    area: float = field(init=False) # Поле не передається в __init__

    def __post_init__(self):
        if self.height <= 0 or self.width <= 0:
            raise ValueError("Height and width must be positive")
        self.area = self.height * self.width
```

### Змінні класу (Class variables)

Змінні класу, які мають анотацію типу, розглядаються як поля датакласу за замовчуванням. 
Якщо змінна класу не повинна бути полем екземпляра, її слід анотувати за допомогою `typing.ClassVar`.

```python
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class MyClass:
    instance_var: int
    class_var: ClassVar[str] = "default_class_value"

obj = MyClass(10)
print(obj.instance_var)    # 10
print(MyClass.class_var)   # default_class_value
# print(obj.class_var)     # Також працює, але це змінна класу
```

### Змінні лише для ініціалізації (Init-only variables)

Іноді потрібно передати дані в `__init__` (і, відповідно, в `__post_init__`), 
які не є полями датакласу. 
Для цього використовується `dataclasses.InitVar`. 
Такі поля передаються в `__post_init__` як аргументи.

```python
from dataclasses import dataclass, InitVar

@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[str] = None # Не буде полем екземпляра

    def __post_init__(self, database):
        if self.j is None and database is not None:
            # self.j = database.lookup('j_for_i', self.i) # Приклад використання
            print(f"Database provided: {database}, i={self.i}")
        else:
            print("No database or j is set.")

c_obj1 = C(10, database="my_db") # Database provided: my_db, i=10
# print(c_obj1.database) # AttributeError: 'C' object has no attribute 'database'
c_obj2 = C(20, 5)                # No database or j is set.
```

### Успадкування (Inheritance)

Датакласи можуть успадковуватися від інших датакласів. Правила наступні:

*   Якщо дочірній клас визначає поля, вони додаються після полів батьківського класу.
*   Якщо дочірній клас перевизначає поле батьківського класу, тип та значення за замовчуванням беруться з дочірнього класу.
*   Порядок полів в генерованому `__init__` такий: спочатку поля батьківського класу, потім поля дочірнього.
*   **Перевпорядкування keyword-only параметрів в `__init__()**: Якщо базовий клас має keyword-only поля, а дочірній клас додає нові позиційні поля, це може призвести до помилки, оскільки всі keyword-only аргументи повинні йти після позиційних. Датакласи автоматично перевпорядковують keyword-only поля з базових класів, щоб вони йшли після всіх позиційних полів, включаючи ті, що додані в дочірніх класах.

```python
from dataclasses import dataclass, field, KW_ONLY

@dataclass
class Base:
    x: int
    y: int = 0
    _: KW_ONLY # Роздільник для keyword-only полів
    z: int = 10

@dataclass
class Derived(Base):
    t: int # Нове позиційне поле
    # z перевизначено як keyword-only в Base, t - позиційне
    # w - нове keyword-only поле
    w: int = field(kw_only=True, default=100)

# Очікуваний __init__ для Derived:
# def __init__(self, x: int, t: int, y: int = 0, *, z: int = 10, w: int = 100):
# Зверніть увагу на порядок: x (Base), t (Derived), y (Base, з default), потім KW_ONLY z (Base), w (Derived)

d = Derived(x=1, t=2, z=30)
print(d) # Derived(x=1, y=0, t=2, z=30, w=100)
```

### `KW_ONLY` для позначення keyword-only полів

Спеціальний маркер `dataclasses.KW_ONLY` (зазвичай присвоюється псевдо-полю з іменем `_`) використовується для позначення того, що всі наступні поля є keyword-only.

```python
from dataclasses import dataclass, KW_ONLY

@dataclass
class Person:
    name: str
    age: int
    _: KW_ONLY # Все, що йде далі, є keyword-only
    city: str = "Unknown"
    country: str

# p = Person("Alice", 30, "New York", "USA") # Помилка: city та country мають бути keyword-only
p = Person("Alice", 30, city="New York", country="USA")
print(p) # Person(name='Alice', age=30, city='New York', country='USA')
```

### Змінні значення за замовчуванням (Mutable default values)

Використання змінних типів (наприклад, `list` або `dict`) як значень за замовчуванням напряму може призвести до того, що всі екземпляри класу будуть спільно використовувати один і той самий об'єкт. Для уникнення цього слід використовувати `default_factory`.

```python
from dataclasses import dataclass, field

# Неправильно:
# @dataclass
# class BadList:
#     items: list = [] # Усі екземпляри будуть ділити цей список

# bad1 = BadList()
# bad1.items.append(1)
# bad2 = BadList()
# print(bad2.items) # Виведе [1]!

# Правильно:
@dataclass
class GoodList:
    items: list = field(default_factory=list)

good1 = GoodList()
good1.items.append(1)
good2 = GoodList()
print(good2.items) # Виведе []
```

### Допоміжні функції модуля `dataclasses`

*   **`fields(dataclass_or_instance)`**: Повертає кортеж об'єктів `Field`, що описують кожне визначене поле для датакласу. Об'єкт `Field` має атрибути: `name`, `type`, `default`, `default_factory`, `init`, `repr`, `hash`, `compare`, `metadata`, `kw_only`.
    ```python
    from dataclasses import fields

    @dataclass
    class Point:
        x: int
        y: int

    for f in fields(Point):
        print(f"Name: {f.name}, Type: {f.type}")
    # Name: x, Type: <class 'int'>
    # Name: y, Type: <class 'int'>
    ```

*   **`is_dataclass(obj)`**: Повертає `True`, якщо `obj` є датакласом або екземпляром датакласу.
    ```python
    from dataclasses import is_dataclass

    print(is_dataclass(Point))      # True
    print(is_dataclass(Point(1,2))) # True
    print(is_dataclass(int))        # False
    ```

*   **`asdict(instance, *, dict_factory=dict)`**: Конвертує екземпляр датакласу `instance` в словник. Кожен датаклас конвертується рекурсивно.
    ```python
    from dataclasses import asdict

    p = Point(10, 20)
    print(asdict(p)) # {'x': 10, 'y': 20}
    ```

*   **`astuple(instance, *, tuple_factory=tuple)`**: Конвертує екземпляр датакласу `instance` в кортеж. Кожен датаклас конвертується рекурсивно.
    ```python
    from dataclasses import astuple

    p = Point(10, 20)
    print(astuple(p)) # (10, 20)
    ```

*   **`make_dataclass(cls_name, fields, *, bases=(), namespace=None, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False, module=None)`**: Динамічно створює новий датаклас.
    *   `cls_name`: Ім'я створюваного класу.
    *   `fields`: Список полів. Кожен елемент може бути рядком (ім'я поля, тип `typing.Any`), кортежем `(name, type)` або `(name, type, field_spec)`.
    *   `bases`: Кортеж базових класів.
    *   `namespace`: Словник для простору імен класу (наприклад, для додавання методів).
    ```python
    from dataclasses import make_dataclass, field

    C = make_dataclass('C',
                       [('x', int),
                        'y', # тип буде typing.Any
                        ('z', int, field(default=5))],
                       namespace={'add_one': lambda self: self.x + 1})

    c_instance = C(10, 'hello')
    print(c_instance)         # C(x=10, y='hello', z=5)
    print(c_instance.add_one()) # 11
    ```

*   **`replace(instance, /, **changes)`**: Створює новий екземпляр того ж типу, що й `instance`, замінюючи поля значеннями з `changes`. Якщо `instance` є `frozen=True`, цей метод все одно працює, оскільки він створює новий об'єкт.
    ```python
    from dataclasses import replace

    @dataclass(frozen=True)
    class User:
        id: int
        name: str

    user1 = User(1, "Alice")
    user2 = replace(user1, name="Bob")
    print(user1) # User(id=1, name='Alice')
    print(user2) # User(id=1, name='Bob')
    ```

### Константи модуля `dataclasses`

*   **`MISSING`**: Спеціальний об'єкт-маркер, що позначає відсутність значення `default` або `default_factory`.
*   **`KW_ONLY`**: Спеціальний маркер типу, який використовується для позначення того, що всі наступні поля в датакласі є keyword-only.

### Обробка винятків

*   **`FrozenInstanceError`**: Підклас `AttributeError`. Викликається, коли неявно визначений метод `__setattr__()` або `__delattr__()` викликається для датакласу, який був визначений з `frozen=True`.

## Нюанси та найкращі практики

*   **Порядок полів**: Порядок полів в `__init__` визначається порядком їх оголошення в класі, з урахуванням успадкування. Поля без значень за замовчуванням повинні йти перед полями зі значеннями за замовчуванням.
*   **`frozen=True`**: Робить екземпляри незмінними, що може бути корисним для використання їх як ключів у словниках або елементів у множинах (якщо вони хешовані).
*   **`default_factory` для змінних типів**: Завжди використовуйте `default_factory=list` (або `dict`, `set` тощо) замість `default=[]`, щоб уникнути несподіваної спільної зміни стану між екземплярами.
*   **`InitVar` та `__post_init__`**: Потужний механізм для складнішої логіки ініціалізації, яка не зберігається безпосередньо як поле.

## Резюме

Датакласи в Python є надзвичайно корисним інструментом, який значно спрощує створення класів для зберігання даних. Вони зменшують кількість шаблонного коду, покращують читабельність та інтегруються з системою типізації Python. Розуміння їхніх можливостей, параметрів декоратора `@dataclass` та функції `field()` дозволяє ефективно використовувати їх у різноманітних сценаріях, від простих структур даних до складніших об'єктів з кастомною логікою ініціалізації та поведінки.
