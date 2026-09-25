from color import Color

class Card:
    def __init__(self, number: str, color: Color | None = None):
        self.number = number
        self.color = color

    def __str__(self):
        if self.color:
            return self.color.paint(self.number)
        return self.number
