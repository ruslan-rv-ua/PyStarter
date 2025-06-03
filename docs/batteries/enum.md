---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Модуль enum

У світі програмування однією з найважливіших складових є робота з константами. 
Модуль `enum` містить інструменти для роботи з контстантами та їх наборами. 
Далі коротко розглянемо деякі з них.

### Enum

`Enum` (від англійського "enumeration" — перелік)) — це тип даних у Python, який дозволяє створювати користувацькі типи даних, що являють собою набір іменованих констант. 

Enum корисний у випадках, коли потрібно обмежити значення змінної певним набором констант. 
Наприклад статус замовлення в інтернет-магазині може мати лише певні визначені значенняя — обробляється, відправлено, доставлено, інші.

Для створення переліка необхідно створити клас успадкований від `Enum`:

```python
from enum import Enum

class OrderStatus(Enum):
    PENDING = 1 # в очікуванні обробки
    PROCESSING = 2 # обробка
    SHIPPED = 3 # відправлено
    DELIVERED = 4 # доставлено
    CANCELLED = 5 # скасовано
```

Можна також скористатись автогенерацією значень:

```python
from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()
```

І навіть зовсім коротко:

```python
import enum

OrderStatus = enum.Enum('OrderStatus', 'PENDING PROCESSING SHIPPED DELIVERED CANCELLED')
```

По перелікам можна ітеруватись. Ітерування відбувається по атрибутам класа. 
Цикл буде йти по елементам у тому порядку, у якому їх вказано при створенні класа. 

    >>> for s in OrderStatus:
    ...     print(s.name, s.value)
    ...
    PENDING 1
    PROCESSING 2
    SHIPPED 3
    DELIVERED 4
    CANCELLED 5
    >>>

Порівнювати елементи можна лише по назві та значенню, 
і лише на рівність та ідентичність:

    >>> status == OrderStatus.PENDING
    True
    >>> status is OrderStatus.PENDING
    True
    >>>
    >>> status < OrderStatus.SHIPPED
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: '<' not supported between instances of 'OrderStatus' and 'OrderStatus'
    >>>
    >>> status is OrderStatus.WAITING
    True

Елементи з однаковими значеннями вказують на один об'єкт:

```python
from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = 1 # в очікуванні обробки
    PROCESSING = 2 # обробка
    SHIPPED = 3 # відправлено
    DELIVERED = 4 # доставлено
    CANCELLED = 5 # скасовано

    WAITING = 1 # те ж, що і PENDING
```

Дослідимо:

    >>> OrderStatus.WAITING is OrderStatus.PENDING
    True
    >>>

Якщо необхідно, щоб усі елементи мали унікальні значення, до класа додаємо декоратор `unique`:

```python
import enum

@enum.unique
class Color(enum.Enum):
    BLACK = 1
    WHITE = 1
```

При спробі виконати вищенаведений код отримаємо `ValueError`:

    @enum.unique
     ^^^^^^^^^^^
    File "C:\Python312\Lib\enum.py", line 1594, in unique
        raise ValueError('duplicate values found in %r: %s' %
    ValueError: duplicate values found in <enum 'Color'>: WHITE -> BLACK
    >>>

### IntEnum

Щоб мати можливість порівнювати елементи по значенням створюємо перелік успадковуючись від класа `IntEnum`:

```python
import enum

class Priority(enum.IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
```

Тепер порівнюємо:

    >>> Priority.CRITICAL > Priority.LOW
    True
    >>>


### StrEnum

Переліки, значеннями елементів якого є символьні рядки. 

```python
import enum

class Color(enum.StrEnum):
    BLACK = 'чорний'
    WHITE = 'білий'

c = Color.BLACK
```

Самі ж елементи "поводяться" теж як символьні рядки:

    >>> c
    <Color.BLACK: 'чорний'>
    >>> c.name
    'BLACK'
    >>> c.value
    'чорний'
    >>> str(c)
    'чорний'
    >>> print(f'Колір: {c}')
    Колір: чорний
	>>> c=='чорний'
	True
	>>>

### Доступ до елементів переліку

Окрім прямого доступу до елементів переліку як до атрибутів класу (наприклад, `OrderStatus.PENDING`), ви можете отримувати доступ до них за іменем (у вигляді рядка) або за значенням.

```python
from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

# Доступ за іменем (атрибут)
status_pending = OrderStatus.PENDING
print(f"Доступ за атрибутом: {status_pending}")

# Доступ за іменем (рядок)
status_shipped = OrderStatus['SHIPPED']
print(f"Доступ за іменем-рядком: {status_shipped}")

# Доступ за значенням
status_cancelled = OrderStatus(5)
print(f"Доступ за значенням: {status_cancelled}")

# Спроба доступу до неіснуючого елемента за іменем призведе до KeyError
# status_invalid_name = OrderStatus['INVALID']

# Спроба доступу до неіснуючого елемента за значенням призведе до ValueError
# status_invalid_value = OrderStatus(10)
```

Результат виконання:

    Доступ за атрибутом: OrderStatus.PENDING
    Доступ за іменем-рядком: OrderStatus.SHIPPED
    Доступ за значенням: OrderStatus.CANCELLED

### Додавання методів до переліків

Класи переліків, як і будь-які інші класи в Python, можуть містити власні методи. Це дозволяє додавати специфічну логіку, пов'язану з елементами переліку.

```python
from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

    def is_terminal(self):
        """Перевіряє, чи є статус кінцевим (доставлено або скасовано)."""
        return self in (OrderStatus.DELIVERED, OrderStatus.CANCELLED)

    def describe(self):
        """Повертає опис статусу."""
        descriptions = {
            OrderStatus.PENDING: "Замовлення очікує обробки.",
            OrderStatus.PROCESSING: "Замовлення в процесі обробки.",
            OrderStatus.SHIPPED: "Замовлення відправлено.",
            OrderStatus.DELIVERED: "Замовлення доставлено.",
            OrderStatus.CANCELLED: "Замовлення скасовано."
        }
        return descriptions.get(self, "Невідомий статус.")

# Використання методів
status1 = OrderStatus.PROCESSING
print(f"Статус: {status1.name}")
print(f"Опис: {status1.describe()}")
print(f"Чи є кінцевим: {status1.is_terminal()}")

status2 = OrderStatus.DELIVERED
print(f"\\nСтатус: {status2.name}")
print(f"Опис: {status2.describe()}")
print(f"Чи є кінцевим: {status2.is_terminal()}")
```

Результат виконання:

    Статус: PROCESSING
    Опис: Замовлення в процесі обробки.
    Чи є кінцевим: False

    Статус: DELIVERED
    Опис: Замовлення доставлено.
    Чи є кінцевим: True


## Додаткові матеріали

- [Документація: enum — Support for enumerations](https://docs.python.org/3/library/enum.html)
- [Документація: Enum HOWTO](https://docs.python.org/3/howto/enum.html#enum-basic-tutorial)
- [Стаття: Build Enumerations of Constants With Python's Enum](https://realpython.com/python-enum/#extending-enumerations-with-new-behavior)