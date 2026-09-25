from typing import List, Optional
from Card import Card

class Column:
    def __init__(self, cards: Optional[List[Card]]):
        self.cards = cards or []
        self.valid_cards(self.cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return ''.join(str(card.number) for card in self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def valid_cards(self, cards: List[Card]):
        combinations = set()

        for card in cards:
            combination = (card.position_x, card.position_x)

            if combination in combinations:
                raise ValueError(f"The {card} is repeated.")

            combinations.add(combination)

        return True

    def add_card(self, card: Card):
        if any(c.position_x == card.position_x and c.position_y == card.position_y for c in self.cards):
            raise ValueError(f"Already exists a card with this values of x and y {card}")

        self.cards.append(card)
