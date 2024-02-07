class EvenNumbers:
    def __init__(self, limit):
        self.even_range = range(0, limit, 2)
    def __contains__(self, item):
        return isinstance(item, int) and item in self.even_range
    
even_numbers = EvenNumbers(10)

r = 10 in even_numbers