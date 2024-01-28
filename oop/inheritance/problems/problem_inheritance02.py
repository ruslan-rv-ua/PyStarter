# ваш код з наступного рядка

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
