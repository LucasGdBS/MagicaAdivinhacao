from Card import Card
from Column import Column
from typing import List
from color import Color

def show_board(board: List[Column]):
    for i in range(7):
        print(f'{board[0][i].__str__()}\t{board[1][i].__str__()}\t{board[2][i].__str__()}')

def ask_column() -> int:
    while True:
        answer = input("Choose a letter and say the column: ")
        if answer in ('1', '2', '3'):
            return int(answer)
        print("Invalid column, type 1, 2 or 3.")

def shuffle(board: List[Column], column: int) -> List[Column]:
    chosen = column - 1

    order = [c for c in range(3) if c != chosen]
    order.insert(1, chosen)
    deck = [card for c in order for card in board[c]]

    new_board = [Column(None) for _ in range(3)]
    for i, card in enumerate(deck):
        new_board[i % 3].add_card(card)

    return new_board


game = [
    Column([Card(chr(ord('A') + i), Color.RED) for i in range(0, 7)]),
    Column([Card(chr(ord('H') + i), Color.GREEN) for i in range(0, 7)]),
    Column([Card(chr(ord('O') + i), Color.MAGENTA) for i in range(0, 7)]),
]

for _ in range(3):
    show_board(game)
    choosed = ask_column()
    game = shuffle(game, choosed)
    print()

print(f'Your card was: {game[1][3]}')
