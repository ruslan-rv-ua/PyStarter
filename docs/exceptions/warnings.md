---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

Бувають ситуації, коли не можна однозначно визначити, чи відбулась помилка у програмі, чи ні. 
Начебто і виникла певна неоднозначна (виняткова) ситуація, 
але програма може продовжувати роботу. 
Було б непогано сповістити про цей факт користувача чи програміста, 
щоб він принаймі знав, що відбулось щось "незвичайне" і звернув на це увагу. 

В Python для цього є механізм так званих "попереджень". 
Це схоже на винятки: 
інформація про виняткову ситуацію виводиться у стандартний потік помилок, 
але програма не припиняє свою роботу. 

Базовим класом для попереджень є `Warning`, який успадковано від `Exception`. 

	>>> Warning
	<class 'Warning'>
	>>> Warning.mro()
	[<class 'Warning'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]
	>>>
	
Від цього класа успадковано класи стандартних для Python попереджень. 
Також ми можемо створити власні попередження, свої класи успадковуємо від `UserWarning`:

	>>> UserWarning.mro()
	[<class 'UserWarning'>, <class 'Warning'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]
	>>> class DeprecatedFeature(UserWarning):
	...     pass
	...
	>>>	

## "Підйом" попереджень

Вивести попередження найпростіше за допомогою функції `warn` з вбудованого модуля `warnings`:

	warn(message, category=UserWarning, stacklevel=1)


* `message` — обов'язковий параметр. Рядок-повідомлення, або екземпляр класа або підкласа Warning (у цьому випадку параметр `category` встановлюється автоматично).
* `category` — опціональний параметр, клас попередження.
* `stacklevel` — рівень вкладеності функцій, починаючи з якого необхідно виводити вміст стека викликів. Корисно, наприклад, для функцій-обгорток для вивода попереджень, де необхідно задати `stacklevel=2`, щоб попередження відносилось до місця виклику даної функції, а не самої функції.

Приклад:

```python
from warnings import warn

class IncorrectNameWarning(UserWarning):
	pass
	
class Person:
	def __init__(self, name):
		if len(name.split()) > 3:
			warn(
				'Name format maybe incorrect:' + name,
				IncorrectNameWarning,
				stacklevel=2
			)
		self._name = name
	@property
	def name(self):
		return self._name
		
		
p = Person('Гассан Абдуррахман ібн Хоттаб')
print(p.name)
print()
p1 = Person('Еріх Марія Ремарк')
print(p1.name)
```		
В результаті виконання цього коду отримаємо приблизно таке:

	c:\dev\warning_test.py:21: IncorrectNameWarning: Name format maybe incorrect:Гассан Абдуррахман ібн Хоттаб
	  p = Person('Гассан Абдуррахман ібн Хоттаб')
	Гассан Абдуррахман ібн Хоттаб
	
	Еріх Марія Ремарк
	
Зверніть увагу, що інтерпретатор повідомив нам, що попередження відноситься до наступного рядка програми: 

	p = Person('Гассан Абдуррахман ібн Хоттаб')
	
Це набагато інформативніше, 
ніж якби нам повідомили, 
що попередження стосується коду в конструкторі класа, 
атже у такому разі невідомо, 
конструювання якого конкретного екземпляра призвело до появи попередження. 
Досягли ми цього задавши параметр `stacklevel=2` для функції `warn`, 
тобто ми почали з другого рівня стеку викликів. 

<!-- ## Фільтрація попереджень

Модуль `warnings` дозволяє гнучко керувати тим, які попередження будуть показуватися, і як саме. Для цього використовується функція

	`warnings.filterwarnings(action, message="", category=Warning, module="", lineno=0, append=False)`.

Основні значення параметра `action`:

*   `"error"`: перетворювати відповідні попередження на винятки.
*   `"ignore"`: ніколи не друкувати відповідні попередження.
*   `"always"`: завжди друкувати відповідні попередження.
*   `"default"`: друкувати перше виникнення відповідного попередження для кожного місця (модуль + номер рядка), де воно виникає.
*   `"module"`: друкувати перше виникнення відповідного попередження для кожного модуля, де воно виникає.
*   `"once"`: друкувати тільки перше виникнення відповідного попередження, незалежно від місця.

Ви також можете вказати `message` (регулярний вираз для тексту попередження), `category` (клас попередження), `module` (регулярний вираз для імені модуля) та `lineno` (номер рядка) для більш точного налаштування фільтрів.

Приклад використання фільтрів:

```python
import warnings

# Визначимо власне попередження
class MyCustomWarning(UserWarning):
    pass

def function_that_warns():
    warnings.warn("Це попередження від function_that_warns!", MyCustomWarning)
    print("Function_that_warns виконана.")

print("--- Демонстрація фільтрації попереджень ---")

# Сценарій 1: Попередження за замовчуванням (якщо не було інших фільтрів)
print("\n1. Попередження за замовчуванням:")
warnings.resetwarnings() # Скидаємо всі фільтри до стану за замовчуванням
# За замовчуванням UserWarning друкується один раз для кожного місця
warnings.simplefilter('always', MyCustomWarning) # Для демонстрації зробимо, щоб завжди друкувалось
function_that_warns()

# Сценарій 2: Ігнорування попереджень
print("\n2. Ігнорування попереджень (MyCustomWarning):")
warnings.filterwarnings("ignore", category=MyCustomWarning)
function_that_warns() # Попередження не буде показано

# Сценарій 3: Перетворення попередження на помилку
print("\n3. Перетворення попередження на помилку (MyCustomWarning):")
warnings.resetwarnings() 
warnings.filterwarnings("error", category=MyCustomWarning)
try:
    function_that_warns()
except MyCustomWarning as e:
    print(f"Спіймано MyCustomWarning як виняток: {e}")
    print("Function_that_warns не була повністю виконана через помилку.")

# Сценарій 4: Показати попередження лише один раз
print("\n4. Показати попередження \'once\':")
warnings.resetwarnings()
warnings.filterwarnings("once", category=MyCustomWarning)
function_that_warns()
function_that_warns() # Друге попередження не буде показано

# Повернемо стандартну поведінку
warnings.resetwarnings()
```

Очікуваний вивід (може дещо відрізнятися залежно від оточення та версії Python, особливо шлях до файлу та номер рядка у повідомленні про попередження):

	--- Демонстрація фільтрації попереджень ---
	
	1. Попередження за замовчуванням:
	__main__:XX: MyCustomWarning: Це попередження від function_that_warns!
	  warnings.warn("Це попередження від function_that_warns!", MyCustomWarning)
	Function_that_warns виконана.
	
	2. Ігнорування попереджень (MyCustomWarning):
	Function_that_warns виконана.
	
	3. Перетворення попередження на помилку (MyCustomWarning):
	Спіймано MyCustomWarning як виняток: Це попередження від function_that_warns!
	Function_that_warns не була повністю виконана через помилку.
	
	4. Показати попередження 'once':
	__main__:XX: MyCustomWarning: Це попередження від function_that_warns!
	  warnings.warn("Це попередження від function_that_warns!", MyCustomWarning)
	Function_that_warns виконана.
	Function_that_warns виконана.

Функція `warnings.simplefilter(action, category=Warning, lineno=0, append=False)` є спрощеною версією `filterwarnings`, яка застосовує фільтр до всіх попереджень вказаної категорії. -->

Детальніше про використання попереджень можна дізнатись з офіційної документації Python.

## Додаткові матеріали

[Документація Python: попередження](https://docs.python.org/3/library/warnings.html)