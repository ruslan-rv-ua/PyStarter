class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented # Важливо для коректної роботи з іншими типами
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        # Хешуємо на основі атрибутів, які використовуються в __eq__
        # Використання кортежу є хорошою практикою, оскільки кортежі незмінні
        # і мають власний коректний __hash__.
        return hash((self.name, self.age))

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

a = Person("Alice", 30)
a2 = Person("Alice", 30) # Такий самий, як a
b = Person("Bob", 25)
