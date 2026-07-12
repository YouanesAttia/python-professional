import math
from typing import List, NamedTuple, Union, Any, Self

class Card(NamedTuple):
    rank: str
    suit: str

class FrenchDeck:
    ranks: List[str] = [str(n) for n in range(2, 11)] + list('JQKA')
    suits: List[str] = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards: List[Card] = [
            Card(rank, suit) 
            for rank in self.ranks 
            for suit in self.suits
        ]
    
    def __len__(self) -> int:
        return len(self._cards)
    
    def __getitem__(self, position: Union[int, slice]) -> Union[Card, List[Card]]:
        return self._cards[position]

class Vector2D:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str: 
        return f'Vector2D({self.x!r}, {self.y!r})'

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other: Any) -> Self:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.__class__(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> Self:
        return self.__class__(self.x * scalar, self.y * scalar)

deck = FrenchDeck()
card_count: int = len(deck)
first_card: Union[Card, List[Card]] = deck[0]

v1 = Vector2D(2, 4)
v2 = Vector2D(2, 1)
v3 = v1 + v2 