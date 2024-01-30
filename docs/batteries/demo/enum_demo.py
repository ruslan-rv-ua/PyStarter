from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = 1 # в очікуванні обробки
    PROCESSING = 2 # обробка
    SHIPPED = 3 # відправлено
    DELIVERED = 4 # доставлено
    CANCELLED = 5 # скасовано

    WAITING = 1 # те ж, що і PENDING
    

status = OrderStatus.WAITING
status is OrderStatus.PENDING

from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()

OrderStatus = Enum('OrderStatus', ['PENDING', 'PROCESSING', 'SHIPPED', 'DELIVERED', 'CANCELLED'])
OrderStatus = Enum('OrderStatus', 'PENDING PROCESSING SHIPPED DELIVERED CANCELLED')


status = OrderStatus.PENDING
r=type(status)
r = status.name, status.value

for s in OrderStatus:
    print(s.name, s.value)

status == OrderStatus.PENDING
status is OrderStatus.PENDING
# status < OrderStatus.SHIPPED


class OrderStatus(Enum):
    PENDING = 1 # в очікуванні обробки
    PROCESSING = 2 # обробка
    SHIPPED = 3 # відправлено
    DELIVERED = 4 # доставлено
    CANCELLED = 5 # скасовано


import enum

#@enum.unique
class Color(enum.Enum):
    BLACK = 1
    WHITE = 1

#################
    
class Priority(enum.IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

Priority.CRITICAL > Priority.LOW

print('-----------------------------')


class Color(enum.StrEnum):
    BLACK = 'чорний'
    WHITE = 'білий'
    
    def __str__(self):
        return self.value.title()

c = Color.BLACK
c.value
print(f'Колір: {c}')



