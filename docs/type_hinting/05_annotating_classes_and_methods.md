## Анотування класів та методів

Розглянемо як анотувати класи та їхні методи, зосереджуючись на актуальних практиках та можливостях останніх версій Python.

### Анотування атрибутів екземпляра та класу

Правильне анотування атрибутів є ключовим для розуміння структури даних класу.

**Атрибути екземпляра** – це дані, унікальні для кожного об'єкта класу. Їх можна анотувати безпосередньо в тілі класу (починаючи з Python 3.6) або в методі `__init__`.

**Атрибути класу** – це дані, спільні для всіх екземплярів класу. Для їх анотації використовується `typing.ClassVar`. Це допомагає статичним аналізаторам відрізнити їх від атрибутів екземпляра, які можуть бути помилково визначені лише на рівні класу.

```python
from typing import ClassVar, List

class Student:
    # Атрибут класу, спільний для всіх екземплярів
    university: ClassVar[str] = "KPI"
    default_faculty: ClassVar[str] # Можна анотувати без значення за замовчуванням

    # Атрибути екземпляра, анотовані в тілі класу
    name: str
    student_id: int
    courses: List[str] # Рекомендовано ініціалізувати в __init__

    def __init__(self, name: str, student_id: int, faculty: str = "FICT") -> None:
        self.name = name
        self.student_id = student_id        self.courses = [] # Ініціалізація атрибута екземпляра
        self.faculty = faculty # Атрибут екземпляра, анотований через __init__

    def enroll(self, course: str) -> None:
        self.courses.append(course)

    def get_info(self) -> str:
        return f"{self.name} (ID: {self.student_id}), Faculty: {self.faculty}, University: {Student.university}"
```

!!! warning "Важливо"
    Якщо атрибут екземпляра анотується в тілі класу, але ініціалізується лише в `__init__`, статичні аналізатори очікуватимуть його ініціалізацію для кожного екземпляра.

### Типи `self` та `cls`

Типи першого аргументу методів екземпляра (`self`) та методів класу (`cls`) зазвичай автоматично виводяться статичними аналізаторами. 
`self` вказує на екземпляр класу, а `cls` – на сам клас.

Однак, існують ситуації, коли явна анотація може бути корисною, особливо для методів, що повертають екземпляр поточного класу. 
<!-- Наприклад, у fluent-інтерфейсах або фабричних методах. -->

#### **`typing.Self` (Python 3.11+)**

Починаючи з Python 3.11, для анотації методів, що повертають екземпляр поточного класу (або його підкласу), 
рекомендується використовувати `typing.Self`. 
Це робить код чистішим та більш виразним.

```python
from typing import Type, Self
# Для Python < 3.11:
# from typing_extensions import Self

class ConfigBuilder:
    settings: dict[str, str]

    def __init__(self) -> None:
        self.settings = {}

    def set_option(self, key: str, value: str) -> Self: # Повертає екземпляр для ланцюжкових викликів
        self.settings[key] = value
        # print(f"Setting {key} = {value}") # для відладки
        return self

    @classmethod
    def from_defaults(cls, default_settings: dict[str, str]) -> Self: # Фабричний метод класу
        # cls() створює екземпляр поточного класу (ConfigBuilder або підкласу)
        builder = cls()
        builder.settings = default_settings.copy()
        return builder

    def build(self) -> dict[str, str]:
        return self.settings

# Використання Self
builder = ConfigBuilder()
config = builder.set_option("mode", "debug").set_option("port", "8080").set_option("host", "localhost").build()
print(f"Config 1: {config}")

# Використання cls у фабричному методі
default_conf = {"user": "admin", "timeout": "30"}
builder_from_defaults = ConfigBuilder.from_defaults(default_conf)
config2 = builder_from_defaults.set_option("retries", "3").build()
print(f"Config 2: {config2}")

# Приклад з підкласом
class AdvancedConfigBuilder(ConfigBuilder):
    def enable_logging(self) -> Self:
        self.settings["logging"] = "enabled"
        return self

adv_builder = AdvancedConfigBuilder.from_defaults({"base": "setting"})
adv_config = adv_builder.set_option("feature", "on").enable_logging().build()
print(f"Advanced Config: {adv_config}")
# `enable_logging` повертає AdvancedConfigBuilder, а `set_option` також коректно працює.
```

Для версій Python до 3.11, замість `Self` можна було використовувати `TypeVar` з обмеженням (`bound=`) на поточний клас, 
або просто рядковий літерал з ім'ям класу. 
`Self` значно спрощує цю задачу.

### Анотація об'єктів класу та самих класів

**Анотація об'єкта (екземпляра) класу** є простою: вказується ім'я класу як тип.

```python
my_instance: MyClass = MyClass()
```

**Анотація самого класу як значення** (наприклад, коли клас передається як аргумент у функцію-фабрику) виконується за допомогою `typing.Type[YourClass]`.

```python
from typing import Type, List, Protocol

class Animal(Protocol): # Використання Protocol для визначення інтерфейсу
    def speak(self) -> str:
        pass # Абстрактний метод

class Dog: # Не обов'язково явно успадковувати Animal, якщо структура співпадає
    def speak(self) -> str:
        return "Гав!"

class Cat:
    def speak(self) -> str:
        return "Няв!"

class SilentAnimal: # Цей клас не реалізує speak
    pass

# Анотація об'єкта класу
my_dog: Dog = Dog()
print(f"My dog says: {my_dog.speak()}")

# Функція, що приймає клас (фабрика), який відповідає протоколу Animal
def create_animal_orchestra(animal_class: Type[Animal], count: int) -> List[Animal]:
    """Створює список тварин заданого типу."""
    orchestra: List[Animal] = []
    for _ in range(count):
        # Створюємо екземпляр переданого класу
        # Type checker перевірить, що animal_class() поверне щось, що має метод speak()
        animal_instance = animal_class()
        orchestra.append(animal_instance)
    return orchestra

# Передача самих класів як значень
dog_orchestra = create_animal_orchestra(Dog, 3) # Dog відповідає протоколу Animal
cat_orchestra = create_animal_orchestra(Cat, 2) # Cat відповідає протоколу Animal

print("\nAnimal Orchestra:")
for animal in dog_orchestra + cat_orchestra:
    print(animal.speak())

# Наступний код викличе помилку статичного аналізатора,
# оскільки SilentAnimal не відповідає протоколу Animal (не має методу speak)
# silent_group = create_animal_orchestra(SilentAnimal, 1)
```

Використання `Type[YourClass]` дозволяє створювати гнучкіші системи, де поведінка може визначатися переданим типом класу.

### Прямі посилання (Forward References)

Пряме посилання виникає, коли анотація типу посилається на ім'я, яке ще не було визначено в поточній області видимості. Це часто трапляється:

1.  При анотуванні атрибута всередині класу, тип якого є сам цей клас (наприклад, вузли дерева, зв'язані списки).
2.  При взаємно рекурсивних залежностях між класами.

Існує два основних способи вирішення цієї проблеми:

**1. Рядкові літерали:** Ім'я типу береться в одинарні або подвійні лапки. Це найстаріший і найнадійніший спосіб, що працює у всіх версій Python, які підтримують анотації.

**2. `from __future__ import annotations` (Python 3.7+):** Цей спеціальний імпорт, розміщений на початку файлу, змушує Python обробляти всі анотації як рядки під час компіляції. Фактичне визначення типів відкладається до моменту, коли вони дійсно потрібні (наприклад, статичним аналізатором). **Це рекомендований сучасний підхід.**

#### Спосіб 1: Використання рядкових літералів

```python
from typing import Optional, List as PyList # Перейменування для уникнення конфлікту з класом List

class Employee:
    name: str
    manager: 'Optional[Employee]' # Пряме посилання на Employee
    subordinates: 'PyList[Employee]'

    def __init__(self, name: str, manager: 'Optional[Employee]' = None) -> None:
        self.name = name
        self.manager = manager
        self.subordinates = []
        if manager:
            manager.add_subordinate(self)

    def add_subordinate(self, employee: 'Employee') -> None:
        self.subordinates.append(employee)

    def __str__(self) -> str:
        manager_name = self.manager.name if self.manager else "None"
        return f"Employee({self.name}, manager={manager_name})"

ceo = Employee("Alice (CEO)")
manager_bob = Employee("Bob (Manager)", manager=ceo)
worker_charlie = Employee("Charlie (Worker)", manager=manager_bob)
worker_diana = Employee("Diana (Worker)", manager=manager_bob)

print(ceo)
print(manager_bob)
print(f"{manager_bob.name}'s subordinates: {[s.name for s in manager_bob.subordinates]}")
print(worker_charlie)
```

#### Спосіб 2: from __future__ import annotations (Python 3.7+)

```python
# Цей імпорт має бути на самому початку файлу.
# from __future__ import annotations # Розкоментуйте, якщо використовуєте цей підхід в окремому файлі

from typing import Optional, List # Тут List вже не конфліктує, бо це інший файл/блок

class Node:
    value: int
    # Завдяки `from __future__ import annotations` (якщо активний),
    # `Node` тут не викликає помилку NameError під час визначення класу.
    # Python обробляє 'Node' як рядок "Node" під капотом.
    left_child: Optional[Node]
    right_child: Optional[Node]

    def __init__(self, value: int) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        return f"Node({self.value})"

# Приклад використання (якщо `from __future__ import annotations` активний)
root = Node(10)
root.left_child = Node(5)
root.right_child = Node(15)
print(f"{root} has left child {root.left_child} and right child {root.right_child}")
```

Використання `from __future__ import annotations` робить код чистішим, оскільки не потрібно брати в лапки кожне пряме посилання.

### Використання `@overload` для перевантаження методів/функцій

Іноді функція або метод класу може приймати різні комбінації типів аргументів і/або повертати різні типи залежно від вхідних даних. 
У таких випадках `typing.overload` дозволяє визначити кілька сигнатур для однієї реалізації.

Це корисно для статичних аналізаторів, щоб вони могли точніше перевіряти типи.

**Правила використання `@overload`:**

1.  Імпортуйте `overload` з модуля `typing`.
2.  Надайте серію декораторів `@overload` для кожної підтримуваної сигнатури. Ці оголошення не повинні мати тіла (використовуйте `...`).
3.  Після всіх `@overload` оголошень надайте фактичну реалізацію функції/методу (без декоратора `@overload`).
4.  Сигнатура реалізації повинна бути достатньо загальною, щоб охопити всі перевантажені сигнатури (часто використовуються `Union`, `Any`, або параметри з типами за замовчуванням).

```python
from typing import overload, Union, List as PyList, Any

class DataProcessor:
    @overload
    def process(self, data: int) -> int: ...

    @overload
    def process(self, data: str) -> str: ...

    @overload
    def process(self, data: PyList[int]) -> int: ... # Приклад: сума списку чисел

    @overload
    def process(self, data: PyList[str]) -> str: ... # Приклад: конкатенація списку рядків

    # Реалізація методу
    def process(self, data: Union[int, str, PyList[int], PyList[str]]) -> Union[int, str]:
        if isinstance(data, int):
            print(f"Processing int: {data}")
            return data * data
        elif isinstance(data, str):
            print(f"Processing str: {data}")
            return data.upper()
        elif isinstance(data, list):
            if all(isinstance(item, int) for item in data):
                print(f"Processing list of ints: {data}")
                return sum(data)
            elif all(isinstance(item, str) for item in data):
                print(f"Processing list of strs: {data}")
                return "".join(data)
            else:
                raise TypeError("Unsupported list item types for processing")
        else:
            # Ця гілка не повинна досягатися, якщо перевантаження коректні
            # і статичний аналізатор використовується.
            raise TypeError("Unsupported data type for processing")

# Приклади використання
processor = DataProcessor()

result_int = processor.process(10) # MyPy визначить тип як int
print(f"Result (int): {result_int}") # 100

result_str = processor.process("hello") # MyPy визначить тип як str
print(f"Result (str): {result_str}") # HELLO

result_list_int = processor.process([1, 2, 3, 4]) # MyPy визначить тип як int
print(f"Result (list[int]): {result_list_int}") # 10

result_list_str = processor.process(["a", "b", "c"]) # MyPy визначить тип як str
print(f"Result (list[str]): {result_list_str}") # "abc"

# Наступний виклик викличе помилку статичного аналізатора (наприклад, MyPy),
# оскільки немає перевантаження для (float) або (list[float])
# processor.process(3.14)
# processor.process([1.0, 2.0])

# Якщо передати змішаний список, виникне TypeError під час виконання
# try:
#     processor.process([1, "a"])
# except TypeError as e:
#     print(e)
```

`@overload` не впливає на поведінку коду під час виконання; це суто інструмент для статичного аналізу.
