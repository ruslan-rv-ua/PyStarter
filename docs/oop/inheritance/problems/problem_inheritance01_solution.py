# ваш код починається з наступного рядка. Юніт-тести знаходяться у кінці файла, використовуйте їх як підказку..
from collections import Counter

class Tesla:
    _models_counter = Counter()

    def __init__(self):
        self._models_counter[self.model] += 1
        self._serial = f'{self.model}{self._models_counter[self.model]:06}'
        
    @property
    def serial(self):
        return self._serial
        
    def __repr__(self):
        return f'<{self.__class__.__name__}, serial={self.serial!r}>'
        
class Tesla3(Tesla):
    model = '3'
    
class TeslaX(Tesla):
    model = 'X'
    
class TeslaS(Tesla):
    model = 'S'
    
'''Умова задачі.
Є наступні моделі автомобілів Tesla:
- "3",
- "S",
- "X".

Реалізуйте три класа у відповідності до моделей: Tesla3, TeslaS, TeslaX.

Кожен автомобіль має унікальний серійний номер вигляду:
<model><number>
де:
- model — модель автомобіля,
- number — порядковий номер випуска автомобіля, окремо для кожної моделі, 6 знаків, нулі попереду якщо це необхідно. 
Наприклад:
"3000001" — серійний номер першого випущеного автомобіля моделі "3".
"3000002" — серійний номер другого випущеного автомобіля моделі "3".
"S000101" — серійний номер сто першого випущеного автомобіля моделі "S".
"X100000" — серійний номер стотисячного випущеного автомобіля моделі "X".

Серійні номери присвоюються автомобілям автоматично, при створенні відповідного екземпляра класа.
Серійний номер доступний лише для читання через властивість `serial` екземпляра класа.

Реалізуйте метод `__repr__()` який повертає символьне представлення екземпляра класа у вигляді:
- "<Tesla3, serial='3000002'>"
- "<TeslaX, serial='X100001'>"
- "<TeslaS, serial='S000001'>"
тобто у представленні присутні ім'я класа і властивість `serial` екземпляра.

Спроектуйте архітектуру так, щоб у разі якщо з'явиться нова модель Tesla, можна було б з мінімальними зусиллями розширити архітектуру, наприклад створивши новий клас `TeslaRoadster`.

Підказки:
1. для доповнення числа нулями на початку можна використати форматовані рядки.
2. може щось стане у нагоді з модуля collections.
'''


    
# юніт-тести
t = Tesla3()
assert t.serial == '3000001'
assert repr(t) == "<Tesla3, serial='3000001'>"
t = Tesla3()
assert t.serial == '3000002'
assert repr(t) == "<Tesla3, serial='3000002'>"
for _ in range(100001):
    t = TeslaX()
assert t.serial == 'X100001'
assert repr(t) == "<TeslaX, serial='X100001'>"
assert repr(TeslaS()) == "<TeslaS, serial='S000001'>"
