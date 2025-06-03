---
hide:
#  - navigation # Hide navigation
- toc        # Hide table of contents
---

# Базові типи в анотаціях Python

Розглянемо, як анотувати найпростіші та найчастіше використовувані типи в Python. 

## Вбудовані типи для анотацій

Python має низку вбудованих типів, які безпосередньо використовуються для анотацій. 
Вони є основою для опису даних у вашому коді.

### `int`

Тип `int` використовується для анотування цілих чисел, як додатних, так і від'ємних.

```python
user_count: int = 100
temperature: int = -5
items_in_cart: int
items_in_cart = 0 
```
Статичні аналізатори перевірять, що змінним, анотованим як `int`, присвоюються саме цілочисельні значення.

### `float`

Тип `float` призначений для анотування чисел, що можуть мати дробову частину.

```python
pi_value: float = 3.14159
balance: float = 1234.50
exchange_rate: float
exchange_rate = 39.75
```
Спроба присвоїти, наприклад, рядок змінній типу `float` буде відзначена статичним аналізатором як помилка.

### `str`

Тип `str` використовується для анотування текстових даних (рядків).

```python
user_name: str = "Guido"
error_message: str = "File not found"
default_path: str
default_path = "/usr/local/bin"
```

### `bool`

Тип `bool` анотує значення, які можуть бути або `True` (істина), або `False` (хибність).

```python
is_active: bool = True
has_permission: bool = False
is_processed: bool
is_processed = check_status() # Функція check_status() має повертати bool
```

### `None` (спеціальний тип)

`None` є спеціальним значенням в Python, що позначає відсутність значення. 
Тип самого `None` — це `NoneType`. 

При анотуванні змінних, які можуть містити `None` або ініціалізуються ним, використовується `None`.

```python
result: None = None
last_error: str | None = None # Змінна може бути рядком або None (Python 3.10+)
# Для старіших версій Python (до 3.10) використовуйте typing.Optional:
# from typing import Optional
# last_error_legacy: Optional[str] = None 
```

Використання `| None` (або `Optional[SomeType]` для Python < 3.10) є дуже поширеним для позначення значень, які можуть бути відсутні. 
Детальніше про `Optional` та об'єднання типів буде розглянуто в наступних розділах.

## Анотування змінних

Анотації типів для змінних були введені в **PEP 526** (Python 3.6). Синтаксис простий:

```python
age: int = 30
name: str = "Python Developer"
is_employed: bool = True
salary: float = 5000.00
configuration: None = None # Якщо змінна спочатку не має значення
```

Сучасні IDE та статичні аналізатори часто можуть автоматично вивести тип змінної, 
якщо їй одразу присвоюється значення. 
Наприклад, 

    `count = 0`
    
буде автоматично розпізнано як `int`). 
Однак, явні анотації підвищують надійність та чіткість коду, особливо у великих проектах.

Подивимось коли явне анотування змінних корисне.

**Ініціалізація без значення:** Якщо змінна оголошується, але її значення буде присвоєно пізніше.

```python
items_count: int # Тип вказано, значення буде присвоєно в циклі або функції
...
items_count = len(items) # Пізніше присвоєння значення
```

**Складні типи або неочевидні значення:** Коли тип не є очевидним з присвоєного значення, або коли значення `None` і змінна може мати інший тип.

```python
# Python 3.10+
current_user: str | None = None 
if user_logged_in():
    current_user = get_username()

# Python < 3.10
# from typing import Optional
# current_user_legacy: Optional[str] = None
```


## Анотування параметрів функцій та значень, що повертаються

Це одна з найперших та найважливіших можливостей, введених **PEP 484**.

Синтаксис наступний:

-   Для параметрів: `parameter_name: type`
-   Для значення, що повертається: `-> type`

```python
def greet_user(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."

def calculate_sum(a: int, b: int) -> int:
    return a + b

def print_message(message: str) -> None: # Якщо функція нічого не повертає
    print(message)
```

Виклик функції з правильними типами

```python
greeting = greet_user("Alice", 30)
total = calculate_sum(10, 20)
print_message("Processing complete.")
```

Статичний аналізатор попередить про помилки тут:

```python
wrong_greeting = greet_user("Bob", "forty") # "forty" не є int
wrong_sum = calculate_sum(5.5, 2)         # 5.5 не є int
print_message(123)                        # 123 не є str
```

### Функції, що не повертають значення

Якщо функція не повертає жодного значення або неявно повертає `None`, 
її тип повернення анотується як `None`.

```python
def log_event(event_details: str) -> None:
    # Запис у лог-файл або вивід у консоль
    print(f"LOG: {event_details}")

result = log_event("User logged in")
print(result) # Виведе: None
```

Це чітко вказує, що від функції не слід очікувати корисного результату присвоєння.

### Використання `typing.Any`

Іноді тип значення може бути дійсно динамічним, або ви працюєте зі старим кодом, де типи важко визначити. 
У таких випадках можна використовувати `typing.Any`. 

`Any` сумісний з будь-яким типом, і будь-який тип сумісний з `Any`. 
Це фактично вимикає перевірку типів для цієї частини коду.

```python
from typing import Any

def process_anything(data: Any) -> Any:
    # ... робимо щось з data ...
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, int):
        return data * 2
    return None # Або інше значення за замовчуванням

result1: Any = process_anything("hello")
result2: Any = process_anything(10)
```

!!! warning "Застереження"
    Використовуйте `Any` обережно. 
    Надмірне використання `Any` нівелює переваги статичної типізації. 
    Намагайтеся бути якомога конкретнішими у ваших анотаціях. 
    Багато конфігурацій статичних аналізаторів (наприклад, MyPy) можуть бути налаштовані так, щоб попереджати про використання `Any` або навіть забороняти його.
