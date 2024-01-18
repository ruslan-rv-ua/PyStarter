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
