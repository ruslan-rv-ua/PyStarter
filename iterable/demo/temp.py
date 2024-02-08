class C:
    def __init__(self, till):
        self.till = till
        self.index = -1
        
    def __next__(self):
        self.index += 1
        if self.index > self.till:
            raise IndexError
        return self.index
        
    def __iter__(self):
        return self
        
        

c = C(1)

for i in c:
    print(i)
    
i=iter(c)