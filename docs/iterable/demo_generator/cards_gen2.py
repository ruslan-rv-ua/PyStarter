from typing import NamedTuple, Generator

class Card(NamedTuple):
    rank: str
    suit: str

    def __str__(self):
        return f"{self.rank}{self.suit}"

class CardsDeck:
    RANKS = "6 7 8 9 10 В Д К Т".split()
    SUITS = "♠ ♣ ♦ ♥".split()

    def __iter__(self) -> Generator[Card, None, None]:
        return (Card(rank, suit) for suit in self.SUITS for rank in self.RANKS)
    
cards_list = list(CardsDeck())

cards = CardsDeck()
spades = ' '.join(str(card) for card in cards if card.suit=='♠')

