from typing import NamedTuple

class Card(NamedTuple):
    rank: str
    suit: str

    def __str__(self):
        return f"{self.rank}{self.suit}"

class CardsDeck:
    RANKS = "6 7 8 9 10 В Д К Т".split()
    SUITS = "♠ ♣ ♦ ♥".split()

    @staticmethod
    def generate():
        for suit in CardsDeck.SUITS:
            for rank in CardsDeck.RANKS:
                yield Card(rank, suit)

    def __iter__(self):
        return self.generate()
    
cards = list(CardsDeck())
print(*cards[:9])
