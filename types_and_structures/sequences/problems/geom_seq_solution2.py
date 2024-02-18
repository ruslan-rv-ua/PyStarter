# ваш код з наступного рядка. Рекомендую спочатку добре розібратись з юніт-тестами.
class _PositiveInteger:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not hasattr(instance, self.name):
            if not isinstance(value, int):
                raise TypeError("value must be an integer")
            if value <= 0:
                raise ValueError("value must be positive")
            setattr(instance, self.name, value)
        else:
            raise AttributeError("attribute is read-only")


class GeometricProgression:
    __slots__ = ("_start", "_ratio", "_length")
    start = _PositiveInteger()
    ratio = _PositiveInteger()
    length = _PositiveInteger()

    def __init__(self, start: int, ratio: int, length: int) -> None:
        self.start = start
        self.ratio = ratio
        self.length = length

    def __getitem__(self, index: int|slice) -> int:
        if isinstance(index, slice):
            return [self[i] for i in range(*index.indices(self.length))]
        if not isinstance(index, int):
            raise TypeError("index must be an integer")
        if index < 0:
            index += self.length
        if not 0 <= index < self.length:
            raise IndexError("index out of range")
        return self.start * self.ratio**index

    def __len__(self) -> int:
        return self.length

    def __repr__(self) -> str:
        return f"GeometricProgression({self.start}, {self._ratio}, {self.length})"


""" "Геометрична прогресія"

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
"""

# юніт-тести, не міняйте наступний код
import unittest  # noqa


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
        with self.assertRaises(TypeError):
            gp["a"]
        with self.assertRaises(TypeError):
            gp[1.5]

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
        self.assertEqual(repr(gp), "GeometricProgression(1, 2, 5)")

    def test_len(self):
        gp = GeometricProgression(1, 2, 5)
        self.assertEqual(len(gp), 5)

    def test_slots(self):
        with self.assertRaises(AttributeError):
            GeometricProgression(1, 2, 5).start = 2

    def test_index_type(self):
        gp = GeometricProgression(1, 2, 5)
        with self.assertRaises(TypeError):
            gp[None]
        with self.assertRaises(TypeError):
            gp['index']
        with self.assertRaises(TypeError):
            gp[1.0]
        with self.assertRaises(TypeError):
            gp[[]]


try:
    unittest.main()
except SystemExit:
    pass

g1 = GeometricProgression(1, 2, 5)
g2 = GeometricProgression(1, 2, 5)
