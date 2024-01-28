# ваш код з наступного рядка
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


'''Умова задачі.
Реалізуйте два класи: `Rectangle` та `Square`, які описують прямокутник та квадрат.
Класи мають властивості:
- `area` - площа
- `perimeter` - периметр
'''


# юніт-тести
r = Rectangle(7, 3)
assert r.area == 21
assert r.perimeter == 20
s = Square(7)
assert s.area == 49
assert s.perimeter == 28
