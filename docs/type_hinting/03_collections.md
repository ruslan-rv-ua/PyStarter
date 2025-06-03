# Колекції

Колекції є фундаментальною частиною Python, дозволяючи зберігати та організовувати групи об'єктів. 
Правильне використання колекцій та їх типізація значно покращують читабельність, надійність та супроводжуваність коду, особливо в великих проектах. 
У цій статті ми детально розглянемо основні вбудовані типи колекцій, їх особливості, методи, а також сучасні підходи до їх типізації з акцентом на Python 3.9 та новіших версіях.

## Списки (`list`)

**Створення списків:**

```python
# Порожній список
empty_list_1: list = []
empty_list_2: list = list()

# Список з елементами
numbers: list[int] = [1, 2, 3, 4, 5]
names: list[str] = ["Анна", "Богдан", "Вікторія"]
mixed_list: list[Any] = [1, "текст", True, 3.14] # Потрібно: from typing import Any
```

З Python 3.9 стандартний тип `list` можна використовувати як генерик безпосередньо для вказівки типу елементів:

- `list[int]`: список цілих чисел.
- `list[str]`: список рядків.
- `list[Any]`: список з елементами будь-якого типу (потребує `from typing import Any`).
- `list[list[float]]`: список, що містить списки дійсних чисел (наприклад, матриця).


## Кортежі (`tuple`)

**Кортеж з фіксованою кількістю елементів різних типів:** `tuple[type1, type2, ..., typeN]`.

    `person_data: tuple[str, int, bool] = ("Іван", 30, True)`


**Кортеж з елементами одного типу довільної довжини:** `tuple[ElementType, ...]`.

    `scores: tuple[float, ...] = (90.5, 88.0, 92.5)`

## Словники (`dict`)


**Типізація словників (Python 3.9+):**

`dict[KeyType, ValueType]`

    `ages: dict[str, int] = {"Alice": 30, "Bob": 25}`

**`TypedDict`:** для словників з фіксованим набором рядкових ключів та визначеними типами значень для кожного ключа. Це забезпечує кращу статичну перевірку.

```python
from typing import TypedDict

class Point(TypedDict):
    x: int
    y: int
    label: str # Python 3.9+
    # Для Python 3.8: label: NotRequired[str] або total=False

point_2d: Point = {"x": 10, "y": 20, "label": "A"}
point_2d_invalid: Point = {"x": 10} # Помилка типізації, відсутнє 'y' та 'label'
```

## Множини (`set`)

**Типізація множин (Python 3.9+):** `set[ElementType]`:

    `unique_numbers: set[int] = {10, 20, 30}`


## Перехід від `typing` до вбудованих генериків (Python 3.9+)

До версії Python 3.9 для типізації генеричних колекцій, таких як списки, словники тощо, необхідно було імпортувати відповідні типи з модуля `typing`:

```python
from typing import List, Tuple, Dict, Set, Any

numbers_old: List[int] = [1, 2, 3]
person_old: Tuple[str, int] = ("Bob", 40)
scores_old: Dict[str, float] = {"math": 90.5, "history": 85.0}
unique_ids_old: Set[int] = {10, 20, 30}
mixed_data_old: List[Any] = [1, "hello", None]
```

PEP 585 (Python 3.9+) запровадив можливість використовувати вбудовані типи колекцій (`list`, `tuple`, `dict`, `set`, `frozenset`, а також `type`) як генерики безпосередньо. 
Це робить код чистішим та зменшує кількість необхідних імпортів.

**Переваги нового синтаксису:**

- **Чистіший код:** Менше "шуму" від імпортів `List`, `Dict` і т.д.
- **Простота:** Легше запам'ятати та використовувати.
- **Узгодженість:** Типи, які використовуються під час виконання (`list()`), тепер ті ж самі, що й для анотацій типів (`list[int]`).

Важливо зазначити, що модуль `typing` все ще залишається важливим для більш складних сценаріїв типізації, 
таких як `Any`, `Callable`, `TypeVar`, `Protocol`, `TypedDict`, `NamedTuple` та інших.

## Спеціалізовані колекції з модуля `collections` та `collections.abc`

Окрім вбудованих колекцій, Python надає модуль `collections` з більш спеціалізованими структурами даних. 
Модуль `collections.abc` (Abstract Base Classes) надає абстрактні базові класи, які корисні для типізації та перевірки, чи об'єкт відповідає певному інтерфейсу колекції.

#### Деякі корисні колекції з `collections`

`collections.deque`: Двостороння черга, що підтримує швидке додавання та видалення елементів з обох кінців.

    `my_deque: collections.deque[int] = collections.deque([1, 2, 3])`

`collections.Counter`: Підклас словника для підрахунку хешованих об'єктів.

    `char_counts: collections.Counter[str] = collections.Counter("abracadabra")`

`collections.defaultdict`: Підклас словника, який викликає фабричну функцію для надання значення за замовчуванням для 
відсутніх ключів.

    `grouper: collections.defaultdict[str, list[int]] = collections.defaultdict(list)`

`collections.namedtuple`: Фабрична функція для створення підкласів кортежів з іменованими полями. Буде розглянута окремо.

`collections.OrderedDict`: Словник, який пам'ятає порядок додавання ключів. З Python 3.7+ стандартний `dict` також зберігає порядок, тому `OrderedDict` менш необхідний, але все ще має деякі відмінності (наприклад, метод `move_to_end` та гарантована поведінка при порівнянні).

#### Типізація з `collections.abc`

Ці класи корисні, коли ви хочете вказати, 
що функція приймає будь-який об'єкт, 
що поводиться як певний тип колекції, 
не обмежуючись конкретною реалізацією (`list`, `tuple` тощо).

- `Sequence[T]`: Для послідовностей (наприклад, `list`, `tuple`, `str`).
- `Mapping[KT, VT]`: Для відображень (наприклад, `dict`).
- `Set[T]`: Для множин.
- `Iterable[T]`: Для будь-якого об'єкта, який можна ітерувати.
- `MutableSequence[T]`, `MutableMapping[KT, VT]`, `MutableSet[T]`: Для змінюваних версій.

```python
import collections # для collections.deque, collections.Counter, etc.
import collections.abc # для Sequence, Mapping, etc.
from typing import TypeVar

T = TypeVar('T')

def print_sequence_elements(seq: collections.abc.Sequence[T]) -> None:
    for element in seq:
        print(element)

def process_mapping(data: collections.abc.Mapping[str, int]) -> None:
    for key, value in data.items():
        print(f"{key}: {value * 2}")

print_sequence_elements([1, 2, 3])          # list
print_sequence_elements(("a", "b", "c"))    # tuple
print_sequence_elements({1, 2, 3})        # Помилка типу, set не є Sequence

process_mapping({"a": 1, "b": 2})           # dict
```
