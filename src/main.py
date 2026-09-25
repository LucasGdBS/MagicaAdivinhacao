from Card import Card
from Column import Column
from typing import List

def show_board(board: List[Column]):
    for i in range(7):
        print(f'{board[0][i].__str__()}\t{board[1][i].__str__()}\t{board[2][i].__str__()}')

def shuffle(board: List[Column], column):

    column_numbers = [1, 2, 3]
    column_numbers.pop(column)

    new_column_1 = Column(None)
    new_column_2 = Column(None)
    new_column_3 = Column(None)

    for i in range(0, 7, 3):
        new_column_1.add_card(Card(board[column][i].change_position((i, 1))))
        new_column_2.add_card(Card(board[column][i+1].change_position((i, 2))))
        new_column_3.add_card(Card(board[column][i+2].change_position((i, 3))))

    for c in column_numbers:
        for i in range(0, 7, 3):
            new_column_1.add_card(Card(board[c][i].change_position((i, 1))))
            new_column_2.add_card(Card(board[c][i+1].change_position((i, 2))))
            new_column_3.add_card(Card(board[c][i+2].change_position((i, 3))))

    return [
        new_column_1,
        new_column_2,
        new_column_3
    ]
    

game = []
for c in range(3):
    game.append(Column([Card(chr(ord('A') + i), i, c+1) for i in range(0, 7)]))
    game.append(Column([Card(chr(ord('H') + i), i, c + 2) for i in range(0, 7)]))
    game.append(Column([Card(chr(ord('O') + i), i, c + 3) for i in range(0, 7)]))


show_board(game)

choosed = int(input("Choose a number and say the column: "))

game = shuffle(game, choosed)

show_board(game)



