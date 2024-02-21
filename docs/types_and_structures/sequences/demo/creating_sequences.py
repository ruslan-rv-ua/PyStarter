class C:
    def __getitem__(self, index):
        print(index)
C()['може тут є індекс?']
########################

s = slice(2, 8, 3)
s.indices(10)

s = slice(50, 51)
s.indices(5) # (5, 5, 1)

s = slice(5, 50, 2) 
s.indices(8)

s = slice(None, None, -1)
s.indices(10) # (9, -1, -1)

########################

class Power2:
    def __init__(self, length: int) -> None:
        self.length = length
    def __getitem__(self, index: int) -> int:
        if not isinstance(index, int):
            raise TypeError('index must be an integer')
        if not 0 <= index < self.length:
            raise IndexError('index out of range')
        return 2**index
    def __len__(self) -> int:
        return self.length

p = Power2(10)
p[9]

for n in Power2(5):
    print(n)

list(Power2(10))

#######################

