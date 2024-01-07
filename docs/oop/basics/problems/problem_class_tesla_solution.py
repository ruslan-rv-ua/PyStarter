# ваш код з наступного рядка. Завдання на кінці файла.
class Tesla3:
    model = "Tesla Model 3"
    
    def __init__(self, serial):
        self.serial = serial
        self.driving = False
        
    def drive(self):
        self.driving = True
        
    def stop(self):
        self.driving = False
        
    def is_driving(self):
        return self.driving
        
    def print_info(self):
        print(f"Модель: {self.model}")
        print(f"Серійний номер: {self.serial}")
        
        
# тести
my_tesla = Tesla3("123321")
assert my_tesla.is_driving() is False
my_tesla.drive()
assert my_tesla.is_driving() is True
my_tesla.stop()
assert my_tesla.is_driving() is False
my_tesla.print_info()

"""Завдання.
Реалізуйте клас "Tesla3" за наступним описом.
1. Клас представляє автомобілі моделі "Tesla Model 3".
2. Кожен автомобіль має серійний номер.
3. Щоб автомобіль почав рухатись викликаємо метод drive().
4. Щоб зупинити автомобіль викликаємо метод stop().
5. Визначити чи рухається автомобіль у даний момент можна за допомогою метода-предиката is_driving().
6. Вивести інформацію про конкретний автомобіль можна за допомогою метода print_info(). Вивід приблизно такий:
```
Модель: Tesla Model 3
Серійний номер: 123321
```
"""