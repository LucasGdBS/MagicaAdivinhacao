from typing import List, Optional
from Card import Card

class Column:
    def __init__(self, cards: Optional[List[Card]]):
        self.cards = cards or []

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return ''.join(str(card.number) for card in self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def add_card(self, card: Card):
        self.cards.append(card)
