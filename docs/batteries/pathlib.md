---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Модуль `pathlib`

Модуль `pathlib` був представлений в Python 3.4 (PEP 428) як об'єктно-орієнтований підхід до роботи зі шляхами файлової системи. Він пропонує більш інтуїтивний та читабельний спосіб маніпулювання шляхами порівняно з традиційним модулем `os.path`.

До появи `pathlib` для роботи зі шляхами в Python переважно використовувався модуль `os.path` разом з іншими функціями з модуля `os`. Цей підхід мав кілька недоліків:

*   **Рядкова репрезентація:** Шляхи представлялися як звичайні рядки, що могло призводити до помилок при конкатенації або маніпуляціях.
*   **Процедурний стиль:** Функції `os.path` працюють у процедурному стилі, що менш зручно для складних операцій.
*   **Платформозалежність:** Деякі аспекти роботи зі шляхами могли відрізнятися на різних операційних системах.

`pathlib` вирішує ці проблеми, надаючи класи для представлення шляхів, методи для виконання операцій над ними та кращу абстракцію від особливостей конкретної ОС.

## Основи: Класи `Path` та `PurePath`

Модуль `pathlib` надає два основні класи для роботи зі шляхами:

*   `PurePath`: Цей клас призначений для маніпуляцій зі шляхами без взаємодії з файловою системою. Він корисний, коли потрібно лише обробляти або конструювати шляхи, не перевіряючи їх існування чи властивості. `PurePath` має підкласи `PurePosixPath` та `PureWindowsPath` для роботи зі шляхами у стилі POSIX та Windows відповідно.
*   `Path`: Цей клас успадковується від `PurePath` і додає методи для взаємодії з файловою системою (створення файлів/директорій, перевірка існування, читання/запис тощо). `Path` також має платформозалежні підкласи `PosixPath` та `WindowsPath`.

Зазвичай, ви будете імпортувати та використовувати клас `Path` напряму:

```python
from pathlib import Path
```

### Створення об'єктів Path

Об'єкт `Path` можна створити з рядка, іншого об'єкта `Path` або навіть з кількох частин шляху:

```python
# З рядка
p1 = Path('/usr/local/bin')
p2 = Path('C:\Users\Default')

# З іншого об'єкта Path
p3 = Path(p1)

# З кількох частин (автоматичне об'єднання)
p4 = Path('/usr', 'local', 'bin')
print(p4)  # Виведе: /usr/local/bin (або \usr\local\bin на Windows)

# Створення шляху до поточного каталогу
current_dir = Path('.')
# або
current_dir_alt = Path() # еквівалентно Path('.')
print(current_dir.resolve()) # Виведе абсолютний шлях до поточного каталогу

# Створення шляху до домашнього каталогу користувача
home_dir = Path.home()
print(home_dir)
```

### Оператор `/` для об'єднання шляхів

Однією з найзручніших особливостей `pathlib` є можливість використовувати оператор `/` для об'єднання шляхів. Це робить код значно чистішим та інтуїтивнішим порівняно з `os.path.join()`.

```python
from pathlib import Path

base_path = Path('/etc')
config_path = base_path / 'nginx' / 'nginx.conf'
print(config_path)  # Виведе: /etc/nginx/nginx.conf

# Можна також об'єднувати з рядками
another_path = Path('/var/log') / 'syslog'
print(another_path) # Виведе: /var/log/syslog
```
Це набагато читабельніше, ніж:
```python
import os
config_path_os = os.path.join('/etc', 'nginx', 'nginx.conf')
```

## Отримання компонентів шляху

Об'єкти `Path` надають зручні атрибути для доступу до різних частин шляху:

*   `.name`: Повне ім'я файлу або останнього компонента шляху (включаючи розширення).
*   `.stem`: Ім'я файлу без розширення.
*   `.suffix`: Розширення файлу (включаючи крапку).
*   `.suffixes`: Список усіх розширень файлу (наприклад, для `archive.tar.gz` це буде `['.tar', '.gz']`).
*   `.parent`: Батьківський каталог.
*   `.parents`: Послідовність батьківських каталогів.
*   `.drive` (для Windows): Буква диска.
*   `.root`: Корінь шляху (наприклад, `/` для POSIX, `\` або `C:\` для Windows).
*   `.anchor`: Комбінація `.drive` та `.root`.

```python
from pathlib import Path

p = Path('/home/user/data/archive.tar.gz')

print(f"Повний шлях: {p}")
print(f"Ім'я файлу: {p.name}")         # archive.tar.gz
print(f"Основа імені: {p.stem}")       # archive.tar
print(f"Розширення: {p.suffix}")       # .gz
print(f"Усі розширення: {p.suffixes}") # ['.tar', '.gz']
print(f"Батьківський каталог: {p.parent}") # /home/user/data
print(f"Корінь: {p.root}")             # /
print(f"Якір: {p.anchor}")           # /

# Батьківські каталоги
print(f"Батьки: {list(p.parents)}")
# [/home/user/data, /home/user, /home, /]

# Для шляхів Windows
win_p = Path('C:\Users\User\Documents\report.docx')
print(f"Диск (Windows): {win_p.drive}") # C:
print(f"Корінь (Windows): {win_p.root}")   # \
print(f"Якір (Windows): {win_p.anchor}") # C:\
```

### Абсолютні та відносні шляхи

*   `.is_absolute()`: Перевіряє, чи є шлях абсолютним.
*   `.resolve(strict=False)`: Перетворює шлях на абсолютний, розкриваючи всі символічні посилання (`..`, `.`). Якщо `strict=True` (за замовчуванням `False` з Python 3.6+), то `FileNotFoundError` буде піднято, якщо шлях не існує.

```python
from pathlib import Path

# Відносний шлях
relative_path = Path('my_folder/my_file.txt')
print(f"'{relative_path}' є абсолютним? {relative_path.is_absolute()}") # False

# Абсолютний шлях
absolute_path = Path('/usr/bin/python3')
print(f"'{absolute_path}' є абсолютним? {absolute_path.is_absolute()}") # True

# Отримання абсолютного шляху
current_file_path = Path('example.txt')
# Створимо файл для демонстрації resolve()
current_file_path.write_text("Hello")

print(f"Абсолютний шлях до '{current_file_path}': {current_file_path.resolve()}")

# Якщо файл не існує, resolve() без strict=True все одно працює (повертає гіпотетичний абсолютний шлях)
non_existent_path = Path('non_existent_dir/file.txt')
print(f"Resolve для неіснуючого шляху: {non_existent_path.resolve()}")

try:
    # З strict=True, якщо шлях не існує, буде помилка
    print(non_existent_path.resolve(strict=True))
except FileNotFoundError as e:
    print(f"Помилка з strict=True: {e}")

# Очистка
current_file_path.unlink()
```

## Перевірка властивостей шляху

Об'єкти `Path` надають низку методів для перевірки характеристик файлу або каталогу, на який вони вказують, без необхідності окремо імпортувати модуль `os`.

*   `.exists()`: Повертає `True`, якщо шлях існує (вказує на файл, каталог, символічне посилання тощо), інакше `False`.
*   `.is_dir()`: Повертає `True`, якщо шлях вказує на існуючий каталог. Якщо це символічне посилання, воно розкривається.
*   `.is_file()`: Повертає `True`, якщо шлях вказує на існуючий звичайний файл. Якщо це символічне посилання, воно розкривається.
*   `.is_symlink()`: Повертає `True`, якщо шлях вказує на символічне посилання.
*   `.is_socket()`: Повертає `True`, якщо шлях вказує на сокет UNIX.
*   `.is_fifo()`: Повертає `True`, якщо шлях вказує на FIFO (іменований канал).
*   `.is_block_device()`: Повертає `True`, якщо шлях вказує на блоковий пристрій.
*   `.is_char_device()`: Повертає `True`, якщо шлях вказує на символьний пристрій.
*   `.samefile(other_path)`: Повертає `True`, якщо цей шлях та `other_path` вказують на той самий файл (використовує `os.path.samefile`). `other_path` може бути рядком або іншим об'єктом `Path`.

```python
from pathlib import Path

# Створимо деякі файли та каталоги для демонстрації
temp_dir = Path('temp_pathlib_demo')
temp_dir.mkdir(exist_ok=True)

my_file = temp_dir / 'my_document.txt'
my_file.write_text("Це тестовий файл.")

my_subdir = temp_dir / 'my_subdirectory'
my_subdir.mkdir()

# Перевірки
print(f"Шлях '{temp_dir}' існує: {temp_dir.exists()}")
print(f"Шлях '{my_file}' існує: {my_file.exists()}")
print(f"Шлях 'non_existent_file.txt' існує: {Path('non_existent_file.txt').exists()}")

print(f"'{temp_dir}' є каталогом: {temp_dir.is_dir()}")
print(f"'{my_file}' є каталогом: {my_file.is_dir()}")

print(f"'{my_file}' є файлом: {my_file.is_file()}")
print(f"'{my_subdir}' є файлом: {my_subdir.is_file()}")

# Створимо символічне посилання (працює на POSIX-системах, на Windows потрібні права адміністратора або режим розробника)
try:
    symlink_path = temp_dir / 'file_link'
    # Переконуємось, що посилання не існує перед створенням
    if symlink_path.exists() or symlink_path.is_symlink():
        symlink_path.unlink()
    symlink_path.symlink_to(my_file)
    print(f"'{symlink_path}' є символічним посиланням: {symlink_path.is_symlink()}")
    print(f"Символічне посилання '{symlink_path}' вказує на файл: {symlink_path.is_file()} (після розкриття)")
    print(f"'{my_file}' та '{symlink_path}' вказують на той самий файл: {my_file.samefile(symlink_path)}")
except OSError as e:
    print(f"Не вдалося створити символічне посилання: {e}")

# Очистка
if 'symlink_path' in locals() and symlink_path.exists():
    symlink_path.unlink()
my_subdir.rmdir()
my_file.unlink()
temp_dir.rmdir()
```

## Операції з файловою системою

Клас `Path` надає методи для виконання більшості поширених операцій з файлами та каталогами.

### Читання файлів

*   `.read_text(encoding=None, errors=None)`: Читає вміст файлу як текст. `encoding` та `errors` мають те саме значення, що й для вбудованої функції `open()`.
*   `.read_bytes()`: Читає вміст файлу як байти.
*   `.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)`: Відкриває файл так само, як вбудована функція `open()`. Повертає файловий об'єкт. Рекомендується використовувати з менеджером контексту (`with`):

```python
from pathlib import Path

# Створимо тестовий файл
file_path = Path('example.txt')
file_path.write_text("Привіт, світ pathlib!\nДругий рядок.", encoding='utf-8')

# Читання тексту
content_text = file_path.read_text(encoding='utf-8')
print(f"Вміст (текст):\n{content_text}")

# Читання байтів
content_bytes = file_path.read_bytes()
print(f"Вміст (байти): {content_bytes}")

# Використання .open()
print("Читання за допомогою .open():")
try:
    with file_path.open(mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
except Exception as e:
    print(f"Помилка при відкритті файлу: {e}")

# Очистка
file_path.unlink()
```

### Запис у файли

*   `.write_text(data, encoding=None, errors=None)`: Записує текстові дані `data` у файл. Якщо файл існує, він перезаписується. Якщо ні, створюється новий.
*   `.write_bytes(data)`: Записує байтові дані `data` у файл. Аналогічно перезаписує або створює новий.

```python
from pathlib import Path

text_file = Path('my_text_output.txt')
text_file.write_text("Перший рядок.\nДругий рядок.", encoding='utf-8')
print(f"Створено файл '{text_file}' з текстом.")

bytes_file = Path('my_binary_output.dat')
bytes_file.write_bytes(b"\x00\x01\x02\x03\x04")
print(f"Створено файл '{bytes_file}' з байтами.")

# Перевірка вмісту (опціонально)
print(f"Вміст '{text_file}':\n{text_file.read_text(encoding='utf-8')}")
print(f"Вміст '{bytes_file}' (байти): {bytes_file.read_bytes()}")

# Очистка
text_file.unlink()
bytes_file.unlink()
```

### Створення каталогів

*   `.mkdir(mode=0o777, parents=False, exist_ok=False)`:
    *   `mode`: Права доступу до каталогу (як у `os.mkdir()`).
    *   `parents`: Якщо `True`, створює батьківські каталоги, якщо вони не існують. Якщо `False` (за замовчуванням) і батьківський каталог не існує, виникає `FileNotFoundError`.
    *   `exist_ok`: Якщо `False` (за замовчуванням) і цільовий каталог вже існує, виникає `FileExistsError`. Якщо `True`, помилка не виникає, якщо каталог існує.

```python
from pathlib import Path

# Просте створення каталогу
dir1 = Path('new_directory')
try:
    dir1.mkdir()
    print(f"Каталог '{dir1}' створено.")
    dir1.rmdir() # Очистка
except FileExistsError:
    print(f"Каталог '{dir1}' вже існує.")

# Створення каталогу з батьківськими та ігноруванням існування
dir2 = Path('parent_dir/child_dir/grandchild_dir')
try:
    dir2.mkdir(parents=True, exist_ok=True)
    print(f"Каталог '{dir2}' та його батьки створені (або вже існували).")
    # Очистка (видаляємо по черзі)
    dir2.rmdir()
    dir2.parent.rmdir()
    dir2.parent.parent.rmdir()
except Exception as e:
    print(f"Помилка при створенні '{dir2}': {e}")
```

### Видалення файлів та каталогів

*   `.unlink(missing_ok=False)`: Видаляє файл або символічне посилання. Якщо `missing_ok=True` і шлях не існує, помилка не виникає. В іншому випадку (і якщо шлях не існує) виникає `FileNotFoundError`.
*   `.rmdir()`: Видаляє порожній каталог. Якщо каталог не порожній, виникає `OSError`.

**Важливо:** `pathlib` не має вбудованого методу для рекурсивного видалення не порожніх каталогів (аналога `shutil.rmtree()`). Для цього потрібно використовувати модуль `shutil`.

```python
from pathlib import Path
import shutil # Для shutil.rmtree

# Створення файлу та каталогу для видалення
file_to_delete = Path('temp_file.txt')
file_to_delete.write_text("Видали мене!")

dir_to_delete_empty = Path('empty_temp_dir')
dir_to_delete_empty.mkdir()

dir_to_delete_non_empty = Path('non_empty_temp_dir')
dir_to_delete_non_empty.mkdir()
(dir_to_delete_non_empty / 'some_file.txt').write_text("Всередині")

# Видалення файлу
if file_to_delete.exists():
    file_to_delete.unlink()
    print(f"Файл '{file_to_delete}' видалено.")
else:
    print(f"Файл '{file_to_delete}' не знайдено для видалення.")

# Видалення порожнього каталогу
if dir_to_delete_empty.exists():
    dir_to_delete_empty.rmdir()
    print(f"Порожній каталог '{dir_to_delete_empty}' видалено.")
else:
    print(f"Каталог '{dir_to_delete_empty}' не знайдено для видалення.")

# Видалення не порожнього каталогу за допомогою shutil.rmtree
if dir_to_delete_non_empty.exists():
    shutil.rmtree(dir_to_delete_non_empty)
    print(f"Не порожній каталог '{dir_to_delete_non_empty}' видалено за допомогою shutil.rmtree.")
else:
    print(f"Каталог '{dir_to_delete_non_empty}' не знайдено для видалення.")

# Спроба видалити неіснуючий файл з missing_ok=True
non_existent_file = Path('i_do_not_exist.txt')
non_existent_file.unlink(missing_ok=True) # Не викличе помилку
print(f"Спроба видалити '{non_existent_file}' з missing_ok=True пройшла без помилок.")
```

### Перейменування та переміщення

*   `.rename(target)`: Перейменовує файл або каталог. `target` може бути рядком або об'єктом `Path`. Якщо `target` існує, поведінка залежить від ОС (на POSIX зазвичай перезаписує, на Windows може викликати помилку, якщо це файл).
*   `.replace(target)`: Перейменовує файл або каталог, атомарно замінюючи `target`, якщо він існує. Це, як правило, більш передбачувана операція, ніж `.rename()` при наявності `target`.

```python
from pathlib import Path

# Створимо файли та каталоги для перейменування/переміщення
base_dir = Path('rename_demo')
base_dir.mkdir(exist_ok=True)

original_file = base_dir / 'original.txt'
original_file.write_text("Оригінальний вміст")

target_file_rename = base_dir / 'renamed_by_rename.txt'
target_file_replace = base_dir / 'renamed_by_replace.txt'

original_dir = base_dir / 'original_folder'
original_dir.mkdir(exist_ok=True)
(original_dir / 'file_in_folder.txt').write_text("Файл у папці")

target_dir_rename = base_dir / 'folder_renamed_by_rename'

# 1. Перейменування файлу за допомогою rename()
if original_file.exists():
    # Переконаємось, що цільовий файл не існує, щоб уникнути перезапису (для демонстрації)
    if target_file_rename.exists():
        target_file_rename.unlink()
    original_file.rename(target_file_rename)
    print(f"Файл '{original_file}' перейменовано на '{target_file_rename}' за допомогою rename().")
else:
    print(f"Файл '{original_file}' не знайдено.")

# Відновимо original_file для наступного тесту
if target_file_rename.exists():
    original_file = base_dir / 'original.txt' # Потрібно оновити шлях, бо об'єкт не змінюється
    target_file_rename.rename(original_file)

# 2. Перейменування/заміна файлу за допомогою replace()
if original_file.exists():
    # Створимо файл, який буде замінено
    if not target_file_replace.exists():
        target_file_replace.write_text("Цей файл буде замінено")

    original_file.replace(target_file_replace)
    print(f"Файл '{original_file}' замінив/перейменувався на '{target_file_replace}' за допомогою replace().")
    # original_file тепер не існує під старою назвою
else:
    print(f"Файл '{original_file}' не знайдено для replace.")

# 3. Перейменування каталогу
if original_dir.exists():
    if target_dir_rename.exists():
        shutil.rmtree(target_dir_rename) # Видалимо, якщо існує, для чистоти тесту
    original_dir.rename(target_dir_rename)
    print(f"Каталог '{original_dir}' перейменовано на '{target_dir_rename}'.")
else:
    print(f"Каталог '{original_dir}' не знайдено.")

# Очистка
shutil.rmtree(base_dir)
```

### Інші операції

*   `.chmod(mode)`: Змінює права доступу до файлу або каталогу (як `os.chmod()`).
*   `.lchmod(mode)`: Те саме, що й `.chmod()`, але не розкриває символічні посилання.
*   `.touch(mode=0o666, exist_ok=True)`: Створює файл за цим шляхом. Якщо файл вже існує, оновлює його час модифікації (як команда `touch` в UNIX), якщо `exist_ok=True` (за замовчуванням). Якщо `exist_ok=False` і файл існує, виникає `FileExistsError`.
*   `.stat()`: Повертає об'єкт `os.stat_result` з інформацією про шлях (метадані файлу).
*   `.lstat()`: Те саме, що й `.stat()`, але для символічних посилань повертає інформацію про саме посилання, а не про файл, на який воно вказує.
*   `.owner()` (POSIX): Повертає ім'я власника файлу.
*   `.group()` (POSIX): Повертає ім'я групи файлу.
*   `.symlink_to(target, target_is_directory=False)`: Створює символічне посилання, що вказує на `target`. Якщо `target_is_directory=True`, посилання створюється як посилання на каталог (важливо на Windows).
*   `.hardlink_to(target)` (Python 3.10+): Створює жорстке посилання, що вказує на той самий inode, що й `target`.

```python
from pathlib import Path
import os
import time

# Створимо файл для демонстрації
file_ops = Path('file_for_ops.txt')
file_ops.write_text("Демонстрація операцій")

# .touch()
print(f"Час модифікації до touch: {file_ops.stat().st_mtime}")
time.sleep(0.01) # Невелика затримка для гарантованої зміни часу
file_ops.touch()
print(f"Час модифікації після touch: {file_ops.stat().st_mtime}")

new_file_touch = Path('newly_touched_file.txt')
if new_file_touch.exists(): new_file_touch.unlink()
new_file_touch.touch()
print(f"Файл '{new_file_touch}' створено за допомогою touch: {new_file_touch.exists()}")
new_file_touch.unlink()

# .chmod() (приклад для POSIX, на Windows може мати обмежену дію)
try:
    original_mode = file_ops.stat().st_mode
    print(f"Початкові права: {oct(original_mode)}")
    # Встановлюємо права тільки на читання для власника
    file_ops.chmod(0o400) # r--------
    print(f"Нові права: {oct(file_ops.stat().st_mode)}")
    # Відновлюємо початкові права
    file_ops.chmod(original_mode)
    print(f"Відновлені права: {oct(file_ops.stat().st_mode)}")
except OSError as e:
    print(f"Помилка chmod: {e} (можливо, недостатньо прав або ОС не підтримує операцію повністю)")

# .stat()
stats = file_ops.stat()
print(f"Розмір файлу '{file_ops}': {stats.st_size} байт")
print(f"Час останнього доступу: {stats.st_atime}")
print(f"Час останньої модифікації: {stats.st_mtime}")
print(f"Час створення (Windows) / зміни метаданих (POSIX): {stats.st_ctime}")

# .owner() та .group() (працюють на POSIX)
try:
    print(f"Власник '{file_ops}': {file_ops.owner()}")
    print(f"Група '{file_ops}': {file_ops.group()}")
except ImportError:
    print("pwd або grp модулі недоступні (ймовірно, не POSIX система) для owner/group.")
except Exception as e:
    print(f"Помилка отримання власника/групи: {e}")

# .symlink_to() та .hardlink_to()
link_target = Path('link_target_file.txt')
link_target.write_text("Файл-ціль для посилань")

symlink_path = Path('my_symbolic_link')
hardlink_path = Path('my_hard_link')

# Видаляємо, якщо існують з попередніх запусків
if symlink_path.is_symlink() or symlink_path.exists(): symlink_path.unlink()
if hardlink_path.exists(): hardlink_path.unlink()

try:
    symlink_path.symlink_to(link_target)
    print(f"Створено символічне посилання '{symlink_path}' -> '{link_target}'")
    print(f"'{symlink_path}' є посиланням: {symlink_path.is_symlink()}")
    print(f"'{symlink_path}' вказує на існуючий файл: {symlink_path.resolve().exists()}")
except OSError as e:
    print(f"Не вдалося створити символічне посилання: {e} (на Windows потрібні права адміністратора або режим розробника)")

try:
    # hardlink_to доступний з Python 3.10
    if hasattr(Path, 'hardlink_to'):
        hardlink_path.hardlink_to(link_target)
        print(f"Створено жорстке посилання '{hardlink_path}' -> '{link_target}'")
        print(f"Статистика '{link_target}': inode={link_target.stat().st_ino}, nlink={link_target.stat().st_nlink}")
        print(f"Статистика '{hardlink_path}': inode={hardlink_path.stat().st_ino}, nlink={hardlink_path.stat().st_nlink}")
    else:
        print("Метод .hardlink_to() недоступний (потрібен Python 3.10+).")
except Exception as e:
    print(f"Не вдалося створити жорстке посилання: {e}")

# Очистка
if symlink_path.is_symlink() or symlink_path.exists(): symlink_path.unlink()
if hardlink_path.exists(): hardlink_path.unlink()
link_target.unlink()
file_ops.unlink()
```

## Ітерація по вмісту каталогу

`pathlib` надає кілька способів для перебору файлів та каталогів всередині директорії.

*   `.iterdir()`: Повертає ітератор по всіх об'єктах `Path` у каталозі (файли, підкаталоги, посилання тощо). Не рекурсивний. Порядок не гарантований.

```python
from pathlib import Path

# Створимо структуру для демонстрації
demo_iter_dir = Path('demo_iterdir')
demo_iter_dir.mkdir(exist_ok=True)
(demo_iter_dir / 'file1.txt').write_text("1")
(demo_iter_dir / 'file2.py').write_text("2")
(demo_iter_dir / 'subdir').mkdir(exist_ok=True)
(demo_iter_dir / 'subdir' / 'file3.md').write_text("3")

print(f"Вміст каталогу '{demo_iter_dir}' (за допомогою iterdir):")
for item in demo_iter_dir.iterdir():
    print(f"  - {item.name} ({ 'каталог' if item.is_dir() else 'файл' if item.is_file() else 'інше'})")

# Очистка
shutil.rmtree(demo_iter_dir) # Використовуємо shutil для рекурсивного видалення
```

### Пошук файлів за шаблоном (globbing)

`pathlib` підтримує пошук файлів за шаблонами, схожий на той, що використовується в командному рядку.

*   `.glob(pattern)`: Повертає генератор, що видає об'єкти `Path` для всіх файлів та каталогів, які відповідають заданому шаблону `pattern` *всередині поточного каталогу `Path`*. Шаблон відносний до цього каталогу.
    *   `*`: Відповідає будь-якій послідовності символів (крім роздільника шляху `/`).
    *   `?`: Відповідає одному будь-якому символу (крім `/`).
    *   `[]`: Відповідає одному символу з набору (наприклад, `[abc]`).
    *   `**`: (Рекурсивний glob, Python 3.5+) Якщо використовується як окремий компонент шляху (наприклад, `**/`), відповідає цьому каталогу та всім підкаталогам рекурсивно.

*   `.rglob(pattern)`: "Рекурсивний glob". Еквівалентно виклику `.glob('**/ ' + pattern)`. Шукає шаблон `pattern` у поточному каталозі та всіх його підкаталогах.

```python
from pathlib import Path
import shutil

# Створимо тестову структуру
base_glob_dir = Path('glob_demo')
base_glob_dir.mkdir(exist_ok=True)

(base_glob_dir / 'file_a.txt').write_text('A')
(base_glob_dir / 'file_b.txt').write_text('B')
(base_glob_dir / 'script.py').write_text('print("Hello")')

sub_glob_dir = base_glob_dir / 'subdir'
sub_glob_dir.mkdir(exist_ok=True)
(sub_glob_dir / 'data_a.txt').write_text('Data A')
(sub_glob_dir / 'image.jpg').write_text('Fake JPG')

sub_sub_glob_dir = sub_glob_dir / 'deeper'
sub_sub_glob_dir.mkdir(exist_ok=True)
(sub_sub_glob_dir / 'notes.txt').write_text('Deeper notes')

print(f"Пошук *.txt в '{base_glob_dir}':")
for txt_file in base_glob_dir.glob('*.txt'):
    print(f"  - {txt_file}")

print(f"\nПошук file_?.txt в '{base_glob_dir}':")
for file_match in base_glob_dir.glob('file_?.txt'):
    print(f"  - {file_match}")

print(f"\nРекурсивний пошук *.txt в '{base_glob_dir}' (за допомогою rglob):")
for txt_file_recursive in base_glob_dir.rglob('*.txt'):
    print(f"  - {txt_file_recursive}")

print(f"\nРекурсивний пошук *.txt в '{base_glob_dir}' (за допомогою glob з **):")
for txt_file_recursive_glob in base_glob_dir.glob('**/*.txt'):
    print(f"  - {txt_file_recursive_glob}")

print(f"\nПошук всіх файлів у '{sub_glob_dir}':")
for item in sub_glob_dir.glob('*'):
    if item.is_file():
        print(f"  - {item}")

# Очистка
shutil.rmtree(base_glob_dir)
```

## Маніпуляції зі шляхами (методи `PurePath`)

Ці методи доступні як для `Path`, так і для `PurePath`, оскільки вони не взаємодіють з файловою системою.

*   `.match(pattern)`: Перевіряє, чи відповідає *весь* шлях (відносно поточного об'єкта `Path`) заданому шаблону `pattern`. Шаблони схожі на ті, що використовуються в `glob`, але `**` має особливе значення.
    *   Повертає `True`, якщо шлях відповідає шаблону, інакше `False`.
    *   Зіставляє відносний шлях. Якщо `Path` абсолютний, `match()` завжди поверне `False`.
    *   Для зіставлення абсолютних шляхів, спочатку зробіть шлях відносним до якогось батька.

```python
from pathlib import Path

p1 = Path('a/b/c.txt')
print(f"'{p1}'.match('*.txt'): {p1.match('*.txt')}")             # False (match працює з компонентами)
print(f"'{p1.name}'.match('*.txt'): {Path(p1.name).match('*.txt')}") # True (якщо розглядати тільки ім'я)
print(f"'{p1}'.match('a/b/*.txt'): {p1.match('a/b/*.txt')}")       # True
print(f"'{p1}'.match('a/**/*.txt'): {p1.match('a/**/*.txt')}")     # True

p_abs = Path('/etc/nginx/nginx.conf')
# p_abs є абсолютним, тому match() поверне False для відносних шаблонів
print(f"'{p_abs}'.match('*.conf'): {p_abs.match('*.conf')}") # False
print(f"'{p_abs}'.match('/etc/**/*.conf'): {p_abs.match('/etc/**/*.conf')}") # False

# Щоб зіставити абсолютний шлях, зробіть його відносним:
relative_to_etc = p_abs.relative_to('/etc') # nginx/nginx.conf
print(f"'{relative_to_etc}'.match('nginx/*.conf'): {relative_to_etc.match('nginx/*.conf')}") # True
```

*   `.relative_to(*other)`: Обчислює шлях, відносний до `other`. Якщо шлях не є підшляхом `other`, виникає `ValueError`.

```python
from pathlib import Path

p = Path('/usr/local/lib/python3.9/site-packages')

rel_to_usr_local = p.relative_to('/usr/local')
print(f"Відносно '/usr/local': {rel_to_usr_local}") # lib/python3.9/site-packages

rel_to_usr = p.relative_to('/usr')
print(f"Відносно '/usr': {rel_to_usr}")         # local/lib/python3.9/site-packages

try:
    p.relative_to('/etc')
except ValueError as e:
    print(f"Помилка relative_to: {e}") # '/usr/local/lib/python3.9/site-packages' does not start with '/etc'
```

*   `.with_name(name)`: Повертає новий шлях з тим самим батьківським каталогом, але іншим ім'ям файлу/каталогу.

```python
from pathlib import Path

p = Path('/usr/share/doc/python3/copyright.txt')
renamed_p = p.with_name('LICENSE.txt')
print(f"Оригінал: {p}")
print(f"З новим ім'ям: {renamed_p}") # /usr/share/doc/python3/LICENSE.txt

# Якщо шлях не має імені (наприклад, корінь або '.'), виникає ValueError
try:
    Path('/').with_name('new_root_name') # Не спрацює
except ValueError as e:
    print(f"Помилка with_name для кореня: {e}")
```

*   `.with_stem(stem)` (Python 3.9+): Повертає новий шлях з тим самим батьківським каталогом та розширенням, але іншою основою імені.

```python
from pathlib import Path

p = Path('images/photos/vacation_2023.raw.jpg')

if hasattr(Path, 'with_stem'): # Перевірка наявності методу (для Python < 3.9)
    new_stem_p = p.with_stem('holiday_pics_final')
    print(f"Оригінал: {p}")
    print(f"З новою основою: {new_stem_p}") # images/photos/holiday_pics_final.jpg

    # Якщо є кілька суфіксів, змінюється лише частина до першого суфікса
    complex_stem_p = Path('archive.tar.gz').with_stem('backup')
    print(f"'{Path('archive.tar.gz')}' з основою 'backup': {complex_stem_p}") # backup.gz
else:
    print("Метод .with_stem() недоступний (потрібен Python 3.9+).")
```

*   `.with_suffix(suffix)`: Повертає новий шлях з тим самим батьківським каталогом та основою імені, але іншим розширенням. Якщо оригінальний шлях не мав розширення, нове розширення додається. Якщо `suffix` порожній рядок, розширення видаляється.

```python
from pathlib import Path

p_txt = Path('report.docx')
p_pdf = p_txt.with_suffix('.pdf')
print(f"'{p_txt}' з суфіксом '.pdf': {p_pdf}") # report.pdf

p_no_ext = Path('README')
p_md = p_no_ext.with_suffix('.md')
print(f"'{p_no_ext}' з суфіксом '.md': {p_md}") # README.md

p_remove_ext = p_txt.with_suffix('')
print(f"'{p_txt}' без суфікса: {p_remove_ext}") # report

# Якщо є кілька суфіксів, замінюється лише останній
multi_suffix = Path('archive.tar.gz')
new_suffix = multi_suffix.with_suffix('.bz2')
print(f"'{multi_suffix}' з суфіксом '.bz2': {new_suffix}") # archive.tar.bz2
```

*   `.joinpath(*other)`: Об'єднує поточний шлях з одним або кількома іншими компонентами шляху. Еквівалентно використанню оператора `/`.

```python
from pathlib import Path

base = Path('/opt/app')
config_file = base.joinpath('config', 'settings.ini')
print(f"Об'єднаний шлях: {config_file}") # /opt/app/config/settings.ini
```

*   `str(path_object)` або `path_object.as_posix()` або `path_object.as_uri()`:
    *   `str(p)`: Повертає рядкове представлення шляху у форматі, прийнятому для поточної ОС (з `\` на Windows, `/` на POSIX).
    *   `p.as_posix()`: Повертає рядкове представлення шляху з прямими слешами (`/`) незалежно від ОС. Корисно для сумісності.
    *   `p.as_uri()`: Повертає шлях як URI `file://...`. Файл повинен бути абсолютним.

```python
from pathlib import Path

# На Windows:
p_win = Path('C:\Windows\System32')
print(f"str(p_win): {str(p_win)}")         # C:\Windows\System32
print(f"p_win.as_posix(): {p_win.as_posix()}") # C:/Windows/System32
print(f"p_win.as_uri(): {p_win.as_uri()}")     # file:///C:/Windows/System32

# На POSIX:
p_posix = Path('/usr/bin/python')
print(f"\nstr(p_posix): {str(p_posix)}")         # /usr/bin/python
print(f"p_posix.as_posix(): {p_posix.as_posix()}") # /usr/bin/python
print(f"p_posix.as_uri(): {p_posix.as_uri()}")     # file:///usr/bin/python
```

## Робота з `__file__`

Часто потрібно отримати шлях до каталогу, де знаходиться поточний скрипт. `pathlib` робить це дуже просто:

```python
# Уявіть, що цей код знаходиться у файлі /path/to/your_project/utils/helpers.py
from pathlib import Path

# Шлях до поточного файлу
current_file_path = Path(__file__)
print(f"Шлях до поточного файлу: {current_file_path}")

# Шлях до каталогу, де знаходиться поточний файл
current_dir_path = Path(__file__).parent
print(f"Каталог поточного файлу: {current_dir_path}")

# Шлях до кореня проекту (наприклад, на два рівні вище)
project_root = Path(__file__).parent.parent.parent # або .resolve().parents[2]
print(f"Корінь проекту (приклад): {project_root}")

# Створення шляху до файлу даних у проекті
data_file = project_root / 'data' / 'my_data.csv'
print(f"Шлях до файлу даних: {data_file}")
```
**Примітка:** Поведінка `__file__` може відрізнятися, якщо скрипт запускається в інтерактивному режимі, запакований (наприклад, PyInstaller) або є частиною zip-архіву.

## Переваги `pathlib` перед `os.path`

1.  **Об'єктно-орієнтований підхід:** Шляхи є об'єктами з методами, а не просто рядками.
2.  **Читабельність:** Операції, такі як об'єднання шляхів (`/`), роблять код чистішим.
3.  **Менше імпортів:** Багато функціональності `os`, `os.path` та `glob` зібрано в одному місці.
4.  **Типізація:** Об'єкти `Path` легше використовувати з інструментами статичного аналізу та перевірками типів.
5.  **Платформонезалежність:** `pathlib` краще абстрагує відмінності між ОС, хоча деякі методи все ще специфічні для платформи (наприклад, `owner()`).
6.  **Легке тестування:** Маніпуляції зі шляхами за допомогою `PurePath` не вимагають доступу до файлової системи, що спрощує тестування.

## Коли `os.path` може бути все ще корисним?

*   **Сумісність зі старим кодом:** Якщо ви працюєте з великою кодовою базою, яка інтенсивно використовує `os.path`, повний перехід може бути недоцільним.
*   **Деякі специфічні функції:** Хоча `pathlib` покриває більшість випадків, деякі рідкісні або низькорівневі функції можуть бути доступні тільки в `os`.
*   **Продуктивність у дуже критичних циклах:** Для надзвичайно великої кількості простих операцій зі шляхами, представленими рядками, `os.path` може мати незначну перевагу в швидкості, хоча для більшості застосунків ця різниця несуттєва і переваги `pathlib` у зручності переважують.

## Приклади використання

### Приклад 1: Рекурсивний пошук файлів та обробка

```python
from pathlib import Path
import shutil

def process_text_file(file_path: Path):
    print(f"Обробка файлу: {file_path}")
    # Тут може бути логіка читання, аналізу або зміни файлу
    content = file_path.read_text(encoding='utf-8')
    print(f"  Перші 30 символів: {content[:30].replace('\n', ' ')}")

# Створимо тестову структуру
search_dir = Path('my_project_files')
search_dir.mkdir(exist_ok=True)
(search_dir / 'config.txt').write_text("налаштування1=значення1\nналаштування2=значення2")
(search_dir / 'main_script.py').write_text("print('Головний скрипт')")

sub_docs = search_dir / 'documents'
sub_docs.mkdir(exist_ok=True)
(sub_docs / 'report.txt').write_text("Це текстовий звіт про виконану роботу.")
(sub_docs / 'notes.md').write_text("# Нотатки\n- Важливий пункт")

sub_images = search_dir / 'images'
sub_images.mkdir(exist_ok=True)
(sub_images / 'logo.png').write_text("бінарні дані png") # імітація

print("Пошук та обробка всіх .txt файлів:")
for text_file in search_dir.rglob('*.txt'):
    if text_file.is_file(): # Переконуємось, що це файл, а не каталог з .txt в імені
        process_text_file(text_file)

# Очистка
shutil.rmtree(search_dir)
```

### Приклад 2: Організація файлів за розширенням

```python
from pathlib import Path
import shutil

# Створимо каталог із різними файлами
source_folder = Path('mixed_files')
source_folder.mkdir(exist_ok=True)

files_to_create = [
    'document1.pdf', 'image1.jpg', 'document2.pdf', 'archive.zip',
    'script.py', 'photo.png', 'text_notes.txt', 'document3.docx'
]
for fname in files_to_create:
    (source_folder / fname).write_text(f"Вміст файлу {fname}")

# Каталог, куди будемо сортувати
target_folder_base = Path('sorted_files')
target_folder_base.mkdir(exist_ok=True)

print(f"Сортування файлів з '{source_folder}' до '{target_folder_base}'")

for f_path in source_folder.iterdir():
    if f_path.is_file():
        extension = f_path.suffix.lstrip('.') # Отримуємо розширення без крапки
        if not extension: # Якщо немає розширення
            extension = 'no_extension'

        target_subfolder = target_folder_base / extension
        target_subfolder.mkdir(exist_ok=True) # Створюємо підкаталог для розширення

        destination_path = target_subfolder / f_path.name
        try:
            # Переміщуємо файл. Використовуємо replace для атомарності
            f_path.replace(destination_path)
            print(f"  Переміщено '{f_path.name}' -> '{destination_path}'")
        except OSError as e:
            print(f"  Помилка переміщення '{f_path.name}': {e}")

print("\nСтруктура після сортування:")
for item in target_folder_base.rglob('*'): # Покажемо всі файли та папки
    indent = '  ' * (len(item.relative_to(target_folder_base).parts) -1)
    print(f"{indent}{item.name}")

# Очистка
shutil.rmtree(source_folder)
shutil.rmtree(target_folder_base)
```

### Приклад 3: Робота з тимчасовими файлами та каталогами

Модуль `tempfile` добре інтегрується з `pathlib`.

```python
from pathlib import Path
import tempfile

# Створення тимчасового файлу
with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp_file_obj:
    temp_file_path = Path(tmp_file_obj.name)
    tmp_file_obj.write(b"Це дані для тимчасового файлу.\n")

print(f"Створено тимчасовий файл: {temp_file_path}")
print(f"Вміст: {temp_file_path.read_text(encoding='utf-8')}")

# Важливо: NamedTemporaryFile з delete=False не видаляється автоматично на Windows
# після закриття. Потрібно видалити вручну.
if temp_file_path.exists():
    temp_file_path.unlink()
    print(f"Тимчасовий файл '{temp_file_path}' видалено.")

# Створення тимчасового каталогу
with tempfile.TemporaryDirectory(prefix='myapp_') as tmp_dir_name:
    temp_dir_path = Path(tmp_dir_name)
    print(f"\nСтворено тимчасовий каталог: {temp_dir_path}")
    print(f"Чи існує каталог всередині with: {temp_dir_path.exists()}")

    # Можна створювати файли всередині
    (temp_dir_path / 'file1.dat').write_text("data1")
    (temp_dir_path / 'file2.dat').write_text("data2")
    print("Файли в тимчасовому каталозі:")
    for item in temp_dir_path.iterdir():
        print(f"  - {item.name}")

print(f"Чи існує каталог після виходу з with: {temp_dir_path.exists()}") # Буде False
```
