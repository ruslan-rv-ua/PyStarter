---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Функції як об'єкти

Пам'ятаєте, що в Python усе є об'єкт? 
І функції тут не вийняток.

### Об'єкт першого класу

Об'єкт називають «об'єктом першого класу», якщо: 

* його може бути збережено у змінній або інших структурах даних;
* його може бути передано в функцію як аргумент;
* його може бути поверненим з функції як результат;
* його може бути створено під час виконання програми;
* він внутрішньо самоідентифікується (не залежить від іменування).

Зауважте що термін «об'єкт» використовується тут у загальному розумінні 
і не обмежується об'єктами мови програмування. 




### Функції як об'єкти першого класу

В Python функції — об'єкти першого класу. 

	>>> def original_function():
	...     print('I am very cool function.')
	...
	>>> original_function
	<function original_function at 0x0000026094F38FE0>
	>>>

При оголошенні функції створюється об'єкт класу `function`, 
і паралельно створються змінна з іменем, 
вказаним після `def`. 
Пам'ятаючи, що змінні в Python — не що інше, як посилання на об'єкти, 
ми легко можемо посилатися на функцію за допомогою іншого імені: 

	>>> original_function()
	I am very cool function.
	>>> function_ref = original_function
	>>> del original_function
	>>> function_ref()
	I am very cool function.
	>>> original_function()
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	NameError: name 'original_function' is not defined
	>>>

Зауважте що об'єкт класу `function` має своє ім'я. 

	>>> function_ref.__name__
	'original_function'
	>>>

#### Приклад: калькулятор

Давайте напишемо примітивний калькулятор 
який буде підтримувати усього чотири арифметичні операції. 
Нехай користувач вводить два операнди і операцію над ними, 
а програма виводить результат. 

```python
def add(a, b):
	return a + b
	
def sub(a, b):
	return a - b
	
def mul(a, b):
	return a * b
	
def div(a, b):
	return a / b
	
operators = {
	'+': add,
	'-': sub,
	'*': mul,
	'/': div,
}

n1 = float(input('Enter first operand: '))
op = input('Enter operator: ')
n2 = float(input('Enter second operand: '))

res = operators[op](n1, n2)

print('Result', res)
```



## Додаткові матеріали

* [Вікіпедія — Об'єкт першого класу](https://uk.wikipedia.org/wiki/Об%27єкт_першого_класу)
