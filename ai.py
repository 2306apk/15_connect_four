import random

from board import COLS


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = [c for c in range(COLS) if board.grid[0][c] == "."]

        for token in (me, opponent):
            for col in legal:
                row = board.drop(col, token)
                wins = board.winner(token)
                board.grid[row][col] = "."
                if wins:
                    return col

        return random.choice(legal) if legal else None
