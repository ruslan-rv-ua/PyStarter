class Sequence:
    def __getitem__(self, index):
        if index in range(1,11):
            return index
        raise IndexError
        
s=Sequence()
for x in s:
    print(x)
