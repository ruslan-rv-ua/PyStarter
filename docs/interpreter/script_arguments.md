---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Передача аргументів скрипту

Нехай для початку у нас є скрипт на Python `hello.py`, і буде це класичний "Hello World". 

	if __name__ == "__main__":
		print('Hello, World!')
	

Виконавши титанічну роботу ми віддали її замовнику. 
Замовник задоволений, але просить додати можливість вказати ім'я того, 
кого вітаємо, причому цей параметр може бути не обов'язковим. 
Тобто програму можна використовувати двома шляхами: 

	python hello.py
	python hello.py Jane
	
Коли ми запускаємо наш скрипт, ми передаємо файл зі скриптом інтерпретатору. 
Але крім цього після назви скрипта інтерпретатору можна також передати додаткові параметри. 
І ці параметри будуть знаходитись у змінній `args` з модуля `sys`. 

Це список. Першим елементом цього списка завжди буде ім'я або шлях до файла нашого скрипта. 
Починаючи з другого елемента списка будуть усі параметри, які ми передавали нашому скрипту. 
Якщо ж параметрів не було передано, то довжина цього списка завжди буде дорівнювати 1. 

Отже тепер ми можемо переписати наш код приблизно так:

```python
from sys import argv

if __name__ == "__main__":
	if len(argv) > 1:
		name = argv[1]
	else:
		name = 'World'
	print(f"hello, {name}!")
```
	
Переконаємось що усе як задумано:

	>python hello.py Вася
	hello, Вася!
	>python hello.py
	hello, World!
	
	
### Бібліотека `argparse`

Для більш зручної роботи з аргументами командного рядка в набір стандартних бібліотек Python включено бібліотеку `argparse`. 
Ця бібліотека дозволяє:

- зручно аналізувати аргументи `sys.argv`
- конвертувати аргументи з символьних рядків у об'єкти вашої програми для подальшої роботи з ними
- форматувати та виводити інформативні підказки для користувача
- багато іншого

Тут ми не розглядаємо детально цю бібліотеку. 
Ознайомитись з її можливостями а також з прикладами використання можна у відповідній документації. 

	
## Додаткові матеріали

- [sys — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)
- [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html)
- [click — Composable command line interface toolkit](https://click.palletsprojects.com/en/8.1.x/)

	
<!--
Windows 7
[HKEY_CLASSES_ROOT\Applications\python.exe\shell\open\command]
@="\"C:\\Python27\\python.exe\" \"%1\" %*"

win10
Computer\HKEY_CLASSES_ROOT\Applications\python.exe
Computer\HKEY_CLASSES_ROOT\py_auto_file\shell\open\command
	was:
		"C:\Python36\python.exe" "%1"
	new:
		"C:\Python36\python.exe" "%1" "%*"
-->
	

	
<!-- https://jenyay.net/Programming/Argparse#noargparse -->