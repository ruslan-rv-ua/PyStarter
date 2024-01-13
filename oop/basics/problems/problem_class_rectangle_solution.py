'''1. Реалізуйте клас Rectangle який описує прямокутник із заданими сторонами. Сторони зберігаються як дійсні числа.
Реалізуйте метод get_area() який повертатиме площу прямокутника.

2. Реалізуйте метод __repr__(). 

3. Реалізуйте метод __str__().
Має повертати символьний рядок такого вида:
[7.0 × 3.0]

4. Для метода get_area() створіть docstring. Прочитайте документацію до метода за допомогою help().

5. Створіть документацію до класа Rectangle. Вивчіть документацію до класа Rectangle.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)
    
    def get_area(self):
        '''Get the area of rectangle.
        
        Returns:
            float: area of the rectangle.
        '''
        return self.width * self.height
    
    def __repr__(self):
        return f'Rectangle({self.width!r}, {self.height!r})'
        
    def __str__(self):
        return f'[{self.width} × {self.height}]'
    
# не міняйте наступний код, це тести
r = Rectangle(7, 3)
assert r.get_area() == 21.0
assert repr(r) == 'Rectangle(7.0, 3.0)'
assert str(r) == '[7.0 × 3.0]'
print(f'Площа прямокутника {r} складає {r.get_area()}')
