import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]
    
    def __len__(self):
        return len(self._card)
    
    def __getitem__(self, position):
        return self._cards[position]    

deck = FrenchDeck()
len(deck)   # 52
deck[0]     # Card(rank='2', suit='spades')
choice(deck)

for card in deck:
    print(card)