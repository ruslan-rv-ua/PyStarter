# Розширені можливості типізації в Python з модулем `typing`

Модуль `typing` надає потужні інструменти для створення більш точних та виразних анотацій типів. 
Це допомагає покращити читабельність коду, полегшує статичний аналіз та зменшує кількість помилок під час розробки. 

## `Any` - Універсальний тип

`Any` є спеціальним типом, який вказує на те, що змінна, параметр функції або значення, що повертається, може бути будь-якого типу. 
Використання `Any` фактично вимикає перевірку типів для конкретного елемента.

Коли використовувати:

- При інтеграції з динамічно типізованим кодом або бібліотеками без анотацій типів.
- Коли тип дійсно невідомий або може бути надто складним для точного визначення на даному етапі.

!!! warning "Застереження"
    Використовуйте `Any` обережно, оскільки це послаблює переваги статичної типізації. Намагайтеся бути якомога конкретнішими з типами, де це можливо.

Приклад:

```python
from typing import Any

def process_item(item: Any) -> None:
    # Ми не знаємо тип 'item', тому можемо робити з ним будь-що,
    # але статичний аналізатор не зможе допомогти виявити помилки.
    print(f"Обробка елемента: {item}")
    if hasattr(item, 'upper'):
        print(item.upper())

process_item("Привіт")
process_item(123)
process_item([1, 2, 3])
```

## `Union` - Об'єднання типів

`Union` дозволяє вказати, що змінна може приймати значення одного з кількох можливих типів.

Синтаксис:

- Традиційний: `Union[Type1, Type2, ...]`
- Python 3.10+: Оператор `|` ( `Type1 | Type2 | ...`)

Приклад:

```python
from typing import Union

def get_item_id(item_id: Union[int, str]) -> str:
    return f"ID елемента: {item_id}"

# Використання Union
print(get_item_id(101))
print(get_item_id("item-abc-789"))

# Сучасний синтаксис (Python 3.10+)
def get_item_id_modern(item_id: int | str) -> str:
    return f"Сучасний ID елемента: {item_id}"

print(get_item_id_modern(202))
print(get_item_id_modern("item-xyz-123"))
```

Усередині функції, яка приймає `Union`, часто потрібно перевіряти фактичний тип значення за допомогою `isinstance()` для безпечної роботи з ним.

```python
def process_identifier(ident: int | str):
    if isinstance(ident, int):
        print(f"Числовий ідентифікатор: {ident + 1}")
    elif isinstance(ident, str):
        print(f"Рядковий ідентифікатор: {ident.upper()}")
```

## `Optional` - Можлива відсутність значення (`None`)

`Optional[T]` вказує, що змінна може мати тип `T` або бути `None`. 
Це еквівалентно `Union[T, None]`.

Синтаксис:

- Традиційний: `Optional[Type]`
- Python 3.10+: `Type | None`

Приклад:

```python
from typing import Optional, Any # Any додано для прикладу профілю

def find_user_by_name(name: str) -> Optional[dict[str, Any]]:
    users_db = {
        "alice": {"id": 1, "email": "alice@example.com"},
        "bob": {"id": 2, "email": "bob@example.com"}
    }
    return users_db.get(name.lower())

# Використання Optional
user_profile = find_user_by_name("Alice")
if user_profile is not None:
    print(f"Знайдено користувача: {user_profile['email']}")
else:
    print("Користувача не знайдено.")

user_profile_none = find_user_by_name("Charlie")
if user_profile_none is None:
    print("Користувача Charlie дійсно не знайдено.")


# Сучасний синтаксис (Python 3.10+)
def find_user_by_id_modern(user_id: int) -> dict[str, Any] | None:
    ...

```

## `Callable` - Типізація функцій та методів

`Callable` використовується для анотації об'єктів, які можна викликати, таких як функції, методи або екземпляри класів з методом `__call__`.

Синтаксис:

- `Callable[[Arg1Type, Arg2Type, ...], ReturnType]` для функцій з конкретними типами аргументів та значення, що повертається.
- `Callable[..., ReturnType]` для функцій з будь-якими аргументами, але конкретним типом повернення.
- `Callable` (або `Callable[..., Any]`) для будь-якого об'єкта, що викликається.

Приклад:

```python
from typing import Callable, Any # Any додано для logger_wrapper

# Функція, яка приймає два цілих числа і повертає ціле число
def add(x: int, y: int) -> int:
    return x + y

# Функція, яка приймає іншу функцію як аргумент
def apply_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return operation(a, b)

result_add = apply_operation(add, 5, 3)
print(f"Результат додавання: {result_add}") # Виведе: Результат додавання: 8

result_subtract = apply_operation(subtract, 10, 4)
print(f"Результат віднімання: {result_subtract}") # Виведе: Результат віднімання: 6

# Приклад з lambda-функцією
result_multiply = apply_operation(lambda x, y: x * y, 6, 7)
print(f"Результат множення: {result_multiply}") # Виведе: Результат множення: 42

# Приклад для функції, що приймає будь-які аргументи
def logger_wrapper(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    print(f"Виклик функції {func.__name__} з аргументами {args} та {kwargs}")
    result = func(*args, **kwargs)
    print(f"Функція {func.__name__} повернула {result}")
    return result

logged_add_result = logger_wrapper(add, 10, 20)
```

## `TypeVar` - Змінні типів для генериків

`TypeVar` дозволяє створювати генеричні функції та класи, які можуть працювати з різними типами даних, зберігаючи при цьому узгодженість типів. 

`TypeVar` діє як заповнювач для типу, який буде визначений під час використання генеричної функції або класу.

Синтаксис:

`T = TypeVar('T')` - створює просту змінну типу.
`T_co = TypeVar('T_co', covariant=True)` - коваріантна змінна типу.
`T_contra = TypeVar('T_contra', contravariant=True)` - контраваріантна змінна типу.
`BoundType = TypeVar('BoundType', bound=SomeClass)` - змінна типу, обмежена певним класом або протоколом.
`ConstrainedType = TypeVar('ConstrainedType', str, bytes)` - змінна типу, обмежена переліком можливих типів.

#### Приклад з генеричною функцією:

```python
from typing import TypeVar, Sequence

T = TypeVar('T') # Створюємо просту змінну типу

def get_first_item(items: Sequence[T]) -> T | None: # Sequence для загальності (list, tuple, str)
    if items:
        return items[0]
    return None
```

Використання з різними типами.

`T` стає int:

```python
first_int = get_first_item([1, 2, 3]) 
```

`T` стає str:

```python
first_str = get_first_item(("a", "b", "c"))
```

Статичний аналізатор може попередити про неоднозначність `T` 
або виведе тип як Union[int, str]:

```python
first_mixed = get_first_item([1, "hello"]) 
```

#### Приклад з обмеженням (bound)

`Number` може бути float або будь-який підтип float (наприклад, int розглядається як підтип float в контексті типізації):

```python
Number = TypeVar('Number', bound=float) 

def add_numbers(a: Number, b: Number) -> Number:
    # У реальному сценарії тут може бути складніша логіка,
    # яка вимагає, щоб 'a' та 'b' підтримували операції для float.
    # Для простоти, припускаємо, що операція '+' визначена.
    # MyPy перевірить, що bound=float підтримує '+'.
    return a + b # type: ignore[operator] # type: ignore потрібен, якщо компілятор не може вивести тип для + з bound
```

Number стає float:

```python
result_float = add_numbers(1.5, 2.5)
```

Number стає float (int сумісний з float):

```python
result_int_as_float = add_numbers(1, 2) 
```

#### Приклад з обмеженням (constraints)

```python
StrOrBytes = TypeVar('StrOrBytes', str, bytes)

def process_text_or_bytes(data: StrOrBytes) -> StrOrBytes:
    if isinstance(data, str):
        return data.upper() # OK, data is str
    else: # data is bytes
        return data.replace(b' ', b'_') # OK, data is bytes

processed_str = process_text_or_bytes("hello world")
processed_bytes = process_text_or_bytes(b"hello world")
```

Детальніше про коваріантність та контраваріантність буде розглянуто в розділі про просунуті теми генериків.

## `Generic` - Створення генеричних класів

Клас `Generic` використовується як базовий клас для створення користувацьких генеричних класів. 
Це дозволяє параметризувати класи змінними типу, створеними за допомогою `TypeVar`.

#### Приклад

```python
from typing import TypeVar, Generic, List, Iterable

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __repr__(self) -> str:
        return f"Stack({self._items})"

# Використання генеричного класу Stack
int_stack = Stack[int]() # Створюємо стек для цілих чисел
int_stack.push(1)

str_stack = Stack[str]() # Створюємо стек для рядків
str_stack.push("hello")
```

Можна також успадковувати від генеричних класів. 
Потрібно знову вказати `T` як параметр типу для `MyExtendedStack`, якщо він використовується всередині

```python
U = TypeVar('U') # Можна використовувати іншу змінну типу, або ту саму T
class MyExtendedStack(Stack[U]): # U передається далі, або Stack[T] якщо T визначено в цьому скоупі
    def extend_from_iterable(self, items: Iterable[U]) -> None:
        for item in items:
            self.push(item)

float_stack = MyExtendedStack[float]()
float_stack.extend_from_iterable([1.1, 2.2, 3.3])
```

## `NewType` - Створення семантично різних типів

`NewType` дозволяє створювати нові типи, які є підтипами існуючих типів на рівні статичного аналізу, але розглядаються як окремі, несумісні типи. 
Це допомагає запобігти логічним помилкам, 
коли різні сутності мають однаковий базовий тип представлення. 
Наприклад, `int` для ID користувача та ID замовлення.

!!! warning "Важливо"
    `NewType` не додає жодних перевірок під час виконання. Це суто інструмент для статичних аналізаторів типу MyPy. Об'єкти, створені за допомогою `NewType`, поводяться як об'єкти базового типу під час виконання.

#### Приклад

```python
from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def get_user_name(user_id: UserId) -> str:
    # Логіка отримання імені користувача за його ID
    return f"User_{user_id}" # user_id тут поводиться як int

def get_product_details(product_id: ProductId) -> str:
    # Логіка отримання деталей продукту за його ID
    return f"Product_{product_id}" # product_id тут поводиться як int
```

Створення екземплярів нових типів:

```python
user_one_id = UserId(12345)
product_A_id = ProductId(67890)
```

MyPy видасть помилку: Expected UserId, got ProductId:

```python
get_user_name(product_A_id)
```

MyPy видасть помилку: Expected UserId, got int

```python
get_user_name(123)
```

Хоча MyPy бачить їх як різні, під час виконання це просто int:

```python
print(f"Тип UserId(123): {type(UserId(123))}") # <class 'int'>
print(f"user_one_id == 12345: {user_one_id == 12345}") # True

Помилка — Expected UserId, got int:

```python
some_int: int = 100
user_id_from_int: UserId = some_int 
```

Потрібно явно викликати конструктор NewType:

```python
user_id_from_int_correct: UserId = UserId(100)
```

## `Literal` - Типізація конкретних літеральних значень

`Literal` дозволяє вказати, що змінна або параметр функції може приймати лише одне з декількох конкретних літеральних значень (рядків, чисел, булевих значень, `None` або Enum).

#### Приклад

```python
from typing import Literal

# Визначення типу для режимів доступу до файлу
FileOpenMode = Literal["r", "rb", "w", "wb", "a", "ab"]

def open_custom_file(filename: str, mode: FileOpenMode) -> None:
    print(f"Відкриття файлу '{filename}' в режимі '{mode}'")

open_custom_file("data.txt", "r")
open_custom_file("image.png", "rb")
```
MyPy видасть помилку Argument "mode" to "open_custom_file" has incompatible type "Literal['x']"; expected "FileOpenMode":

```python
open_custom_file("log.txt", "x") # 
```

Literal може містити різні типи літералів

```python
ResponseStatus = Literal[200, 400, 404, 500, "OK", "Error", True, None]

def handle_response_status(status: ResponseStatus) -> None:
    if status == 200 or status == "OK" or status is True:
        print("Все гаразд!")
    elif status == 404:
        print("Ресурс не знайдено.")
    elif status is None:
        print("Статус не визначено.")
    else:
        print(f"Сталася помилка або інший статус: {status}")

handle_response_status(200)
handle_response_status("Error")
handle_response_status(True)
handle_response_status(None)
```

MyPy видасть помилку:

```python
# handle_response_status(301)
```

`Literal` особливо корисний для параметрів, які керують поведінкою функції, де набір допустимих значень обмежений і відомий заздалегідь.

## `Final` - Позначення констант та неперевизначуваних елементів

`Final` використовується для позначення змінних, атрибутів класів або методів, які не повинні бути перепризначені або перевизначені. Статичні аналізатори типів, такі як MyPy, перевіряють ці обмеження.

Використання:

- **Змінні/Атрибути**: `variable: Final[type] = value`
- **Методи**: Декоратор `@final` (з `typing` або `typing_extensions` для старіших версій Python).

#### Приклад

```python
from typing import Final, final

# Глобальна константа
API_VERSION: Final[str] = "v1.2.3"
API_VERSION = "v2.0.0" # MyPy видасть помилку: Cannot assign to final name "API_VERSION"

class Configuration:
    DEBUG_MODE: Final[bool]
    DEFAULT_TIMEOUT: Final[int] = 100 # Можна ініціалізувати тут

    def __init__(self, debug: bool) -> None:
        self.DEBUG_MODE = debug # Final атрибути можна ініціалізувати в __init__
        self.DEFAULT_TIMEOUT = 200 # MyPy видасть помилку, якщо вже ініціалізовано при оголошенні
                                     # і це не перше присвоєння в __init__ для цього екземпляра.

    self.DEBUG_MODE = False # MyPy видасть помилку поза __init__ (або якщо це перепризначення)

    @final
    def get_settings_summary(self) -> str:
        return f"Debug: {self.DEBUG_MODE}, Timeout: {self.DEFAULT_TIMEOUT}"

class AdvancedConfiguration(Configuration):
    # Не можна перевизначити метод, позначений як @final
    def get_settings_summary(self) -> str: # MyPy видасть помилку: Cannot override final method "get_settings_summary"
        return "Advanced summary"
    pass

config = Configuration(debug=True)
print(config.get_settings_summary())
config.DEFAULT_TIMEOUT = 50 # MyPy видасть помилку: Cannot assign to final attribute "DEFAULT_TIMEOUT"
config.DEBUG_MODE = False # MyPy видасть помилку: Cannot assign to final attribute "DEBUG_MODE"
```

`Final` допомагає чіткіше виразити наміри в коді та запобігти випадковим змінам важливих значень або поведінки.

## `TypedDict` - Типізація словників з фіксованою структурою

`TypedDict` дозволяє визначати типи для словників, які мають фіксований набір рядкових ключів, і для кожного ключа – певний тип значення. Це схоже на структуру даних або інтерфейс для словників.

Синтаксис:

```python
from typing import TypedDict, NotRequired # NotRequired з Python 3.11+ або typing_extensions

class MyDictType(TypedDict):
    key1: type1
    key2: type2
    optional_key: NotRequired[type3] # NotRequired для необов'язкових ключів
```

### `NotRequired` та `Required`

- `NotRequired[T]`: Вказує, що ключ може бути відсутнім у словнику. Доступний в `typing` з Python 3.11+, для старіших версій використовуйте `typing_extensions.NotRequired`.
- `Required[T]`: Явно вказує, що ключ є обов'язковим. Це корисно, якщо `TypedDict` визначено з `total=False`, але деякі ключі все одно мають бути обов'язковими. Доступний в `typing` з Python 3.11+, для старіших версій використовуйте `typing_extensions.Required`.

За замовчуванням, усі ключі в `TypedDict` є обов'язковими (`total=True`). 

Щоб зробити всі ключі необов'язковими за замовчуванням, можна передати `total=False` при визначенні `TypedDict`:
`class MyPartialDict(TypedDict, total=False): ...`

#### Приклад з NotRequired

```python
from typing import TypedDict, List, NotRequired, Required

class Movie(TypedDict):
    title: str
    year: int
    director: str
    genres: List[str]
    rating: NotRequired[float] # Цей ключ може бути відсутнім
    budget: NotRequired[int | None] # Може бути відсутнім, або None, якщо присутній

# Приклад з total=False, де більшість ключів необов'язкові
class PartialMovieInfo(TypedDict, total=False):
    title: Required[str] # title обов'язковий, навіть якщо total=False
    year: int            # year необов'язковий
    director: str        # director необов'язковий

def print_movie_details(movie: Movie) -> None:
    print(f"Назва: {movie['title']} ({movie['year']})")
    print(f"Режисер: {movie['director']}")
    print(f"Жанри: {', '.join(movie['genres'])}")
    if 'rating' in movie and movie['rating'] is not None: # Перевірка наявності та значення
        print(f"Рейтинг: {movie['rating']:.1f}/10")
    else:
        print("Рейтинг: не вказано або відсутній")
    
    if 'budget' in movie:
        if movie['budget'] is not None:
            print(f"Бюджет: ${movie['budget']:,}")
        else:
            print("Бюджет: невідомий (None)")
    else:
        print("Бюджет: не вказано")


movie_data: Movie = {
    "title": "Inception",
    "year": 2010,
    "director": "Christopher Nolan",
    "genres": ["Sci-Fi", "Thriller", "Action"],
    "rating": 8.8,
    "budget": 160000000
}

another_movie_data: Movie = {
    "title": "The Matrix",
    "year": 1999,
    "director": "Wachowskis",
    "genres": ["Sci-Fi", "Action"],
    # Ключ 'rating' відсутній, 'budget' також
}

movie_with_none_budget: Movie = {
    "title": "Tenet",
    "year": 2020,
    "director": "Christopher Nolan",
    "genres": ["Action", "Sci-Fi"],
    "budget": None # Допустимо, оскільки тип budget: NotRequired[int | None]
}

print_movie_details(movie_data)
print("-" * 20)
print_movie_details(another_movie_data)
print("-" * 20)
print_movie_details(movie_with_none_budget)


# Приклад використання PartialMovieInfo
partial_info: PartialMovieInfo = {"title": "Dune"} # Тільки title, year і director необов'язкові
# partial_info_invalid: PartialMovieInfo = {"year": 2021} # MyPy видасть помилку: "title" is missing

# MyPy видасть помилку, якщо:
# - відсутній обов'язковий ключ: missing_director: Movie = {"title": "Test", "year": 2022, "genres": []}
# - неправильний тип значення: wrong_year_type: Movie = {"title": "Test", "year": "2022", "director": "N/A", "genres": []}
# - присутній зайвий ключ (якщо total=True): extra_key: Movie = {..., "country": "USA"}
```

## `Protocol` - Структурна типізація (Duck Typing)

`Protocol` дозволяє визначати інтерфейси на основі структурної сумісності (duck typing). 
Клас неявно реалізує протокол, якщо він має всі атрибути та методи, визначені в протоколі, з відповідними сигнатурами. 
Явне успадкування від протоколу не є обов'язковим, але може використовуватися для чіткості та перевірки реалізації статичним аналізатором (MyPy це перевірить, якщо клас успадковує протокол).

Синтаксис:

```python
from typing import Protocol

class MyProtocol(Protocol):
    attribute: SomeType # Атрибут, який має бути присутнім
    
    def method(self, arg: ArgType) -> ReturnType:
        pass

    def method_with_default(self) -> int:
        return 0 # Протоколи можуть мати реалізації за замовчуванням
```

Методи в протоколі можуть мати реалізацію за замовчуванням. 
Якщо клас, що реалізує протокол, не надає власну реалізацію такого методу, використовується реалізація з протоколу.

### `@runtime_checkable`

Декоратор `@runtime_checkable` (з `typing` або `typing_extensions` для старіших версій Python) дозволяє використовувати `isinstance()` та `issubclass()` з протоколами під час виконання. 
Без нього `isinstance()` з протоколом зазвичай викликає `TypeError`. 
Використання `@runtime_checkable` може мати невеликий вплив на продуктивність.

#### Приклад

```python
from typing import Protocol, runtime_checkable, List, Any

@runtime_checkable # Дозволяє isinstance() перевірки під час виконання
class Serializable(Protocol):
    def serialize(self) -> str: ... # Метод, який має бути реалізований

class HasName(Protocol):
    name: str # Атрибут, який має бути присутнім

class User: # Не успадковує явно від Serializable або HasName
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name # Відповідає HasName
        self.email = email

    def serialize(self) -> str: # Відповідає Serializable
        return f'{{"id": {self.user_id}, "name": "{self.name}", "email": "{self.email}"}}'

class Product: # Не успадковує явно
    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name # Відповідає HasName
        self.price = price

    def serialize(self) -> str: # Відповідає Serializable
        return f'{{"product_id": "{self.product_id}", "name": "{self.name}", "price": {self.price}}}'

class NonSerializableData:
    def __init__(self, data_val: Any): # data перейменовано на data_val
        self.data_val = data_val
    # Не має методу serialize() і атрибуту name

def save_to_json_string(items: List[Serializable]) -> List[str]:
    return [item.serialize() for item in items]

def print_names(items: List[HasName]) -> None:
    for item in items:
        print(item.name)


user1 = User(1, "Alice", "alice@example.com")
product1 = Product("prod123", "Laptop", 999.99)
non_serializable_obj = NonSerializableData({"key": "value"}) # non_serializable перейменовано

# MyPy коректно обробить ці виклики
serialized_items = save_to_json_string([user1, product1])
print(f"Серіалізовані елементи: {serialized_items}")

print_names([user1, product1])
# print_names([non_serializable_obj]) # MyPy видасть помилку, бо NonSerializableData не має атрибуту 'name'
# save_to_json_string([non_serializable_obj]) # MyPy видасть помилку, бо NonSerializableData не має методу 'serialize'

# Перевірка під час виконання завдяки @runtime_checkable для Serializable
print(f"user1 is Serializable: {isinstance(user1, Serializable)}") # True
print(f"product1 is Serializable: {isinstance(product1, Serializable)}") # True
print(f"non_serializable_obj is Serializable: {isinstance(non_serializable_obj, Serializable)}") # False

# HasName не є @runtime_checkable, тому isinstance(user1, HasName) викличе TypeError
# print(f"user1 is HasName: {isinstance(user1, HasName)}") # TypeError

# Явна реалізація протоколу (допомагає MyPy перевірити клас)
class Logger(Protocol):
    def log(self, message: str) -> None: ...

class ConsoleLogger: # Явно не успадковує, але відповідає
    def log(self, message: str) -> None:
        print(f"LOG: {message}")

def use_logger(logger: Logger, text: str):
    logger.log(text)

my_logger = ConsoleLogger()
use_logger(my_logger, "Системна подія")
```

## Псевдоніми типів (Type Aliases)

Псевдоніми типів дозволяють створювати більш зрозумілі або короткі назви 
для складних, довгих або часто використовуваних анотацій типів. 
Це покращує читабельність коду та полегшує рефакторинг.

Синтаксис.

Просте присвоєння (усі версії Python):

```python
`MyAlias = complex_type_annotation`
```

Спеціальний синтаксис `type` (Python 3.12+, PEP 695):

```python
`type MyAlias = complex_type_annotation`
```

Цей новий синтаксис чіткіше вказує на намір створення псевдоніма типу 
і може підтримуватися інструментами статичного аналізу краще. 
Він також дозволяє створювати генеричні псевдоніми типів: 

```python
`type ListOrTuple[T] = list[T] | tuple[T, ...]`.
```

#### Приклад

```python
from typing import List, Dict, Tuple, Union, Optional, Any

# Традиційні псевдоніми
Vector = List[float]
Point2D = Tuple[int, int]
Headers = Dict[str, str]
JSONValue = Union[str, int, float, bool, None, Dict[str, Any], List[Any]]
JSONDict = Dict[str, JSONValue]
MaybeString = Optional[str] # Еквівалент Union[str, None] або str | None

def scale_vector(vector: Vector, scalar: float) -> Vector:
    return [x * scalar for x in vector]

def print_point(point: Point2D) -> None:
    print(f"X: {point[0]}, Y: {point[1]}")

def process_request(url: str, headers: Headers) -> JSONDict:
    print(f"Запит до {url} з заголовками: {headers}")
    # ... логіка запиту ...
    return {"status": "success", "data": ["item1", 2]}

user_name: MaybeString = "Alice"
user_name_none: MaybeString = None

# Використання псевдонімів покращує читабельність
def process_coordinates(points: List[Point2D]) -> None:
    for p in points:
        print_point(p)
```

Псевдоніми з новим синтаксисом (Python 3.12+):
<!-- Також цей синтаксис не можна використовувати всередині функцій або класів. -->

```python
type Coordinates = tuple[float, float]
type Identifier = int | str
type StringOrNone = str | None # Сучасний аналог Optional[str]
type Result[T] = tuple[bool, T | None] # Генеричний псевдонім типу

def calculate_distance(p1: Coordinates, p2: Coordinates) -> float:
    # ... логіка обчислення відстані ...
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx**2 + dy**2)**0.5

def fetch_data(uid: Identifier) -> Result[str]:
    if isinstance(uid, int) and uid == 1:
        return (True, "Data for 1")
    if isinstance(uid, str) and uid == "test":
        return (True, "Test data")
    return (False, None)

user_id: Identifier = 123
item_name: StringOrNone = "Book"

success, data = fetch_data(user_id)
if success:
    print(f"Fetched: {data}")
```

Псевдоніми типів не створюють нових типів. 
Вони просто дають інше ім'я існуючому типу. 
Особливо корисні для складних генериків, об'єднань або для надання семантичного значення простим типам у певному контексті.

---

Використання цих розширених типів з модуля `typing` значно підвищує надійність та супроводжуваність Python-коду, особливо у великих проектах та при роботі в команді. 
Статичні аналізатори, такі як MyPy, можуть використовувати ці анотації для виявлення потенційних помилок ще до запуску програми.
