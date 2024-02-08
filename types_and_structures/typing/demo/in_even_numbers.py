class EvenNumbers:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __contains__(self, item):
        if not isinstance(item, int):
            raise ValueError()
        return item % 2 == 0
    
r = 2 in EvenNumbers()

e1 = EvenNumbers()
e2 = EvenNumbers()
r = e1 is e2