---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Обчислювані властивості

**Обчислювані властивості** — це властивості, які можуть бути обчислені. Вони відрізняються від звичайних властивостей тим, що їх не потрібно ініціалізувати, і їх значення може змінюватися протягом життя об’єкта.

Обчислювані властивості зазвичай використовуються для зберігання інформації, яка залежить від інших властивостей об’єкта. 
Наприклад, можна використовувати обчислювану властивість для отримання площі прямокутника:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    @property
    def area(self):
        return self.width * self.height
```

Тепер щоб дізнатись площу прямокутника можна використовувати властивість:

	>>> r = Rectangle(7, 9)
	>>> r.area
	63
	>>>

## Приклад: конвертер температур

Давайте створимо клас у якому будемо зберігати значення температури, наприклад температури повітря. 
У різних країнах температуру повітря вимірюють по різних шкалах: 
в Україні — за Цельсієм, у, наприклад, США — за шкалою Фаренгейта. 
Спроектуємо наш клас таким чином, щоб з температурою можна було б працювати одразу у двох системах. 

Перше що зробимо, це з'ясуємо як перевести температуру з градусів Цельсія у градуси Фаренгейта і навпаки:

	fahrenheit = celsius *  9/5 + 32
    celsius = (fahrenheit -32)* 5/9
	
Спроектуємо наш клас наступним чином:

- температуру будемо зберігати у градусах цельсія у властивості `celsius`
- якщо нам треба дізнатись температуру по Фаренгейту, ми звертатимемось до властивості `fahrenheit`. 
Гетер автоматично переводитиме значення у градуси Фаренгейта використовуючи значення атрибута `celsius`.
- сеттер властивості `fahrenheit` буде встановлювати значення властивості `celsius`

Клас спроектовано, залишається, як завжди, записати це мовою Python:

```python
class TemperatureConverter:
    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('Temperature below -273.15°C is not possible')
        self._celsius = value

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    def __repr__(self) -> str:
        return f'TemperatureConverter({self.celsius})'
    
    def __str__(self) -> str:
        return f'{self.celsius}°C'
```

Скористаємось:

	>>> t = TemperatureConverter()
	>>> t
	TemperatureConverter(0)
	>>> print(t)
	0°C
	>>> t.fahrenheit
	32.0
	>>> t.fahrenheit = 451
	>>> t
	TemperatureConverter(232.77777777777777)
	>>> t.celsius
	232.77777777777777
	>>> t = TemperatureConverter(-1000)
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	File "e:\dev\PyStarter\docs\oop\encapsulation\demo\5e_computed_props.py", line 15, in __init__
		self.celsius = celsius
		^^^^^^^^^^^^
	File "e:\dev\PyStarter\docs\oop\encapsulation\demo\5e_computed_props.py", line 24, in celsius
		raise ValueError('Temperature below -273.15°C is not possible')
	ValueError: Temperature below -273.15°C is not possible
	>>>

