from typing import Union, Tuple

class Card:
    def __init__(self, number=int, position_x=int, position_y=int):
        self.number = number
        self.position_x = position_x
        self.position_y = position_y

    def __str__(self):
        return f"Card = {self.number}, x = {self.position_x}, y = {self.position_y}"

    @property
    def tuple(self) -> tuple:
        return (self.number, self.position_x, self.position_y)
    
    def change_position(self, position:Union[Card, Tuple[int, int]]):
        if isinstance(position, Card):
            self.position_x = position.position_x
            self.position_y = position.position_y
            return Card(self.number, self.position_x, self.position_y)

        if isinstance(position, Tuple):
            if len(position) == 2:
                self.position_x = position[0]
                self.position_y = position[1]
            else:
                raise ValueError(f"The position tuple has {len(position)} items, it should have 2 ")
            return Card(self.number, self.position_x, self.position_y)

        raise ValueError(f"Invalid type for position: {type(position)}. Use a Card or a Tuple[int, int]")

