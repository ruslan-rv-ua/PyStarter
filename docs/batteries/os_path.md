# Модуль path

Модуль `path` вбудовано в модуль `os`. 
Він дозволяє працювати зі шляхами до файлів та папок.

### `os.path.abspath(path)`

Повертає повний шлях до папки/файла. 

	:::python
    os.path.abspath("1.txt")
    # /home/ilnurgi/1.txt

### `os.path.basename(path)`
    
- ***Parameters:***	`path (str)` – шлях до файла/папки

Повертає рядок, ім'я файла чи папки.

	:::python
    >>> os.path.basename('c:\\system\\apps\\Python\\Python.app')
    'Python.app'

### `os.path.dirname(path)`
- ***Parameters:***	`path (str)` – шлях до файла

Повертає рядок, шлях до батьківської папки файла

	:::python
    >>> os.path.dirname ('c:\\system\\apps\\Python\\Python.app')
    'c:\\system\\apps\\Python'

### `os.path.exists(path)`

Повертає `bool`, `True|False`, чи існує вказаний шлях

	:::python
    >>> os.path.exists(u'/home/ilnurgi/')
    True

### `os.path.expanduser(username)`

* ***username*** - str, им'я користувача

Повертає шлях до користувацької папки. 

	:::python
    expanduser('~')
    # 'c:\\users\\ilnurgi\\'

### `os.path.getatime(path)`

- ***Parameters***:	path – шлях до файла
- ***Raises:***	WindowsError – якщо файла не існує

Повертає час останнього доступа до файла чи папки (кількість секунд з початку епохи).

### `os.path.getctime(path)`

- ***Parameters:***	path – шлях до файла
- ***Raises:*	WindowsError – якщо файла не існує

Повертає дату створення файла чи папки (кількість секунд з початку епохи).

### `os.path.getmtime(path)`

- ***Parameters:*	path – шлях до файла
- ***Raises:***	WindowsError – якщо файла не існує

Повертає час останнього внесення змін до файла або папки. 

### `os.path.getsize(path)`

- ***Parameters:***	path – шлях до файла
- ***Raises:***	WindowsError – якщо файла не існує

Повертає розмір файла чи папки

### `os.path.join(path1, path3, ...)`

Об'єднує шляхи.

	:::python
    >>> os.path.join('c:\\', 'system\\apps\\Python\\', 'Python.app')
    'c:\\system\\apps\\Python\\Python.app'

### `os.path.isabs(path)`

- ***Parameters:***	path (str) – путь к файлу/папке
- ***Returns:***	True или False

Перевіряє шлях на абсолютність. 

### `os.path.isdir(path)`

Повертає булеве, чи є вказаний шлях каталогом. 

	:::python
    >>> os.path.isdir(u'/home/ilnurgi/')
    True

### `os.path.isfile(path)`

- ***Parameters:*	path (str) – шлях до папки чи файла

Перевіряє чи вказує шлях на файл. 

### `os.path.islink(path)`

Перевіряє, чи вказує шлях на символічне посилання. 

	:::python
    os.path.islink("path1/1.txt")
    # True

### `os.path.normpath(path)`

- ***Parameters:***	path (str) – шлях до файла чи татки

Повертає рядок, нормалізований шлях відповідно до операційної системи. 

	:::python
    >>> р = os.path.join(r"C:\\", "book/folder/", "file.txt")
    >>> os.path.normpath(p)
    'C:\\book\\folder\\file.txt'

### `os.path.realpath(path)`

Повертає шлях до файла по символічному посиланню (Linux). 

	:::python
    os.path.realpath("symlink_path")
    # "real_path"

### `os.path.split(path)`

- ***Parameters:***	path (str) – шлях до файла

Повертає кортеж з пари рядків - (шлях до батьківської папки, назва файла).

	:::python
    >>> os.path.split('c:\\system\\apps\\Python\\Python.app')
    ('c:\\system\\apps\\Python\\', 'Python.app')

### `os.path.splitdrive(path)`

- ***Parameters:*	path (str) – шлях до файла

Повертає кортеж з пари рядків - (им'я диска, решта шляху).

	:::python
    >>> os.path.splitdrive ('c:\\system\\apps\\Python\\Python.app')
    ('c:\\', 'system\\apps\\Python\\Python.app')

### `os.path.splitext(path)`

- ***Parameters:*	path (str) – шлях до файла

Повертає кортеж з пары рядків - (шлях до файла без розширення, розширення файла). 

	:::python
    >>> os.path.splitext ('c:\\system\\apps\\Python\\Python.app')
    ('c:\\system\\apps\\Python\\Python', '.app')

## Додаткові матеріали

- [Документація: модуль `os.path`](https://docs.python.org/3/library/os.path.html)