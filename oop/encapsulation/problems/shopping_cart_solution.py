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
    """Class to describe item"""
    def __init__(self, name, price):
        """Initializer.
        
        Args:
            name (str): Item's name
            price (float): Item's price
        """
        self._name = name
        self.price = price

    @property
    def name(self):
        """Item's name.
        
        Returns:
            str: Item's name
        """
        return self._name

    @property
    def price(self):
        """Item's price.
        
        Returns:
            float: Item's price
        """
        return self._price
    
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be negative or zero")
        self._price = value

    def __str__(self):
        return f"{self.name} - {self.price:.2f}"
    
    def __repr__(self):
        return f"Item({self.name!r}, {self.price!r})"

class ShoppingCart:
    """Class to describe shopping cart"""
    def __init__(self):
        self._items = []

    def add_item(self, item, count=1):
        """Add item to cart
        
        Args:
            item (Item): item to add
            count (int, optional): number of items. Defaults to 1.
        """
        self._items.extend([item] * count)

    @property
    def total_price(self):
        """total price of all items.
        
        Returns:
            float: total price"""
        return sum(item.price for item in self._items)

    @property
    def items_count(self):
        """total number of items.
        
        Returns:
            int: total number of items
        """
        return len(self._items)
    
    @property
    def items_names(self):
        """sorted list of items names.
        
        Returns:
            list: sorted list of items names
        """
        return sorted(set(item.name for item in self._items))
    
    def __str__(self):
        return f"{self.items_count} items - {self.total_price:.2f}"
    
    def __repr__(self):
        return f"<ShoppingCart, {self.items_count} items>"

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
