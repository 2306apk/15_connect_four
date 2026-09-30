from board import Board
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("Connect Four — you are X.")
        while True:
            self.board.print()
            if self.turn == "X":
                raw = input("Column (1-7), or q: ").strip().lower()
                if raw == "q":
                    return
                try:
                    col = int(raw) - 1
                except ValueError:
                    print("Enter a column number.")
                    continue
            else:
                col = self.ai.choose_column(self.board)

            if col is None:
                self.board.print()
                print("Draw.")
                return

            row = self.board.drop(col, self.turn)
            if row is None:
                print("Column unavailable.")
                continue

            print(f"{self.turn} placed a disc in column {col + 1}.")

            if self.board.winner(self.turn):
                self.board.print()
                print(self.turn, "wins!")
                return
            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            self.turn = "O" if self.turn == "X" else "X"
