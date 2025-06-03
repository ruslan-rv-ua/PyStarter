from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(0.5, 3.0)

print(p1 == p2)  # False
print(p1 < p2)   # False (порівнює спочатку x, потім y)

# p1.x = 5.0  # Викличе dataclasses.FrozenInstanceError
