# ваш код з наступного рядка. Рекомендую спочатку добре розібратись з юніт-тестами.
class GeometricProgression:
    def __init__(self, start: int, ratio: int, length: int) -> None:
        self._start = self._validate_positive_int(start)
        self._ratio = self._validate_positive_int(ratio)
        self._length = self._validate_positive_int(length)
    @staticmethod
    def _validate_positive_int(value) -> int:
        if not isinstance(value, int):
            raise TypeError('value must be an integer')
        if value <= 0:
            raise ValueError('value must be positive')
        return value
    @property
    def start(self) -> int:
        return self._start
    @property
    def ratio(self) -> int:
        return self._ratio
    def __getitem__(self, index: int) -> int:
        if isinstance(index, slice):
            return [self[i] for i in range(*index.indices(self._length))]
        if not isinstance(index, int):
            raise TypeError('index must be an integer')
        if index < 0:
            index += self._length
        if not 0 <= index < self._length:
            raise IndexError('index out of range')
        return self.start * self.ratio ** index
    def __len__(self) -> int:
        return self._length
    def __repr__(self) -> str:
        return f'GeometricProgression({self._start}, {self._ratio}, {self._length})'
    
''' "Геометрична прогресія"

Реалізувати послідовність GeometricProgression, яка представляє геометричну прогресію.
Вхідні параметри:
- start - початкове значення прогресії, ціле число > 0
- ratio - знаменник прогресії, ціле число > 0
- length - кількість елементів прогресії, ціле число > 0
Реалізувати валідацію вхідних параметрів: тип, значення.
Послідовність повинна мати наступні властивості доступні лише для читання:
- start
- ratio
Реалізувати отримання елемента послідовності по індексу, у тому числі по від'ємному.
Реалізувати отримання зрізання послідовності.
Реалізувати визначення довжини послідовності.
Реалізувати представлення послідовності у вигляді символьного рядка.
'''

# юніт-тести, не міняйте наступний код
import unittest # noqa

class TestGeometricProgression(unittest.TestCase):
    def test_properties(self):
        gp = GeometricProgression(1, 2, 5)
        self.assertEqual(gp.start, 1)
        self.assertEqual(gp.ratio, 2)
        with self.assertRaises(AttributeError):
            gp.start = 2
        with self.assertRaises(AttributeError):
            gp.ratio = 3
    def test_indices(self):
        gp = GeometricProgression(1, 2, 5)
        self.assertEqual(gp[0], 1)
        self.assertEqual(gp[1], 2)
        self.assertEqual(gp[2], 4)
        self.assertEqual(gp[3], 8)
        self.assertEqual(gp[4], 16)
        self.assertEqual(gp[-1], 16)
        self.assertEqual(gp[-2], 8)
        self.assertEqual(gp[-3], 4)
        self.assertEqual(gp[-4], 2)
        self.assertEqual(gp[-5], 1)
    def test_wrong_indices(self):
        gp = GeometricProgression(1, 2, 5)
        with self.assertRaises(IndexError):
            gp[5]
        with self.assertRaises(IndexError):
            gp[-6]
    def test_slices(self):
        gp = GeometricProgression(1, 2, 5)
        self.assertEqual(gp[:], [1, 2, 4, 8, 16])
        self.assertEqual(gp[1:], [2, 4, 8, 16])
        self.assertEqual(gp[:-1], [1, 2, 4, 8])
        self.assertEqual(gp[1:-1], [2, 4, 8])
        self.assertEqual(gp[::2], [1, 4, 16])
        self.assertEqual(gp[1::2], [2, 8])
        self.assertEqual(gp[::-1], [16, 8, 4, 2, 1])
        self.assertEqual(gp[::-2], [16, 4, 1])
        self.assertEqual(gp[3::-2], [8, 2])
        self.assertEqual(gp[3:1:-2], [8])
        self.assertEqual(gp[5:], [])
        self.assertEqual(gp[:5], [1, 2, 4, 8, 16])
        self.assertEqual(gp[-6:-8], [])
    def test_repr(self):
        gp = GeometricProgression(1, 2, 5)
        self.assertEqual(repr(gp), 'GeometricProgression(1, 2, 5)')
    def test_len(self):
        gp = GeometricProgression(1, 2, 5)
        self.assertEqual(len(gp), 5)

try:
    unittest.main()
except SystemExit:
    pass

