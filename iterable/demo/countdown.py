class CountDown:
    def __init__(self,  count_from):
        self.counter = count_from + 1
        
    def __next__(self):
        self.counter -= 1
        if self.counter > 0:
            return str(self.counter)
        elif self.counter == 0:
            return "start"
        else:
            raise StopIteration
            
    def __iter__(self):
        return self
            
for c in CountDown(5):
    print(c)
    
c=iter(CountDown(2))
