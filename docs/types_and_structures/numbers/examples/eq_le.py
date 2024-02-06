class V:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value
    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

        
v1 = V(1)
v2 = V(1)
v3 = V(2)
l = [V(777), v3, v2, v1, v3]
# l.sort()