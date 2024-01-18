"""Створити програму за описом. Якщо у задачі щось не убумовлено — дійте на власний розсуд.
Намагайтесь використати усі доступні на даний момент навички і знання.

1. Створити клас `Item` який описує товар.
Клас `Item` має містити:
- атрибут `name`, назва товара. Значення атрибута змінити не можна.
- атрибут `price`, ціна товара. Значення атрибута можна змінити.

2. Створити клас `ShoppingCart`. Клас описує кошик товарів.
Клас `ShoppingCart` має містити:
- метод `add_item(item, count)`, який додає count одиниць товара item до кошика. Якщо count не вказано, то по замовчуванню 1.
- властивість `total_price`, яка повертає загальну вартість усіх товарів.
- властивість `items_count`, яка повертає загальну кількість товарів у кошику.
- властивість `items_names`, яка повертає відсортований список назв товарів у кошику.

3. Для обох класів реалізуйте методи `__str__` та `__repr__`.
"""

# ваш код починається з наступного рядка
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class _ItemInCart:
    def __init__(self, item, count):
        self.item = item
        self.count = count
    
class ShoppingCart:
    def __init__(self):
        self._items = []
    def add_item(self, item, count=1):
        self._items.append(_ItemInCart(item, count))
        
    @property
    def items_count(self):
        count = 0
        for cart_item in self._items:
            count += cart_item.count
        return count
        
    @property
    def items_names(self):
        names = []
        for cart_item in self._items:
            names.append(cart_item.item.name)
        return sorted(names)
        
    @property
    def total_price(self):
        total = 0
        for cart_item in self._items:
            total += cart_item.item.price * cart_item.count
        return total

# далі тести, не модифікувати
cart = ShoppingCart()
cart.add_item(Item("banana", 2.0), 2)
cart.add_item(Item("apple", 1.5))
assert cart.items_count == 3
assert cart.items_names == ["apple", "banana"]
assert cart.total_price == 5.5

cherry = Item("cherry", 3.0)
cart.add_item(cherry)
assert sorted(cart.items_names) == ["apple", "banana", "cherry"]
assert cart.total_price == 8.5
cherry.price = 3.5
assert cart.total_price == 9.0

print(cherry)
print(cart)
