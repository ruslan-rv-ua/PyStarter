class EvenNumbers:
    def __contains__(self, item):
        return isinstance(item, int) and item % 2 == 0
    
even_numbers = EvenNumbers()

r = 2 in even_numbers