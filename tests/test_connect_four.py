import builtins
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from ai import AI
from board import Board, COLS, ROWS
from game import Game


class BoardTests(unittest.TestCase):
    def test_horizontal_win(self):
        board = Board()
        for col in range(4):
            board.drop(col, "X")
        self.assertTrue(board.winner("X"))

    def test_vertical_win(self):
        board = Board()
        for _ in range(4):
            board.drop(0, "O")
        self.assertTrue(board.winner("O"))

    def test_down_right_diagonal_win(self):
        board = Board()
        for row, col in ((2, 0), (3, 1), (4, 2), (5, 3)):
            board.grid[row][col] = "X"
        self.assertTrue(board.winner("X"))

    def test_down_left_diagonal_win(self):
        board = Board()
        for row, col in ((2, 6), (3, 5), (4, 4), (5, 3)):
            board.grid[row][col] = "O"
        self.assertTrue(board.winner("O"))

    def test_three_in_a_row_is_not_a_win(self):
        board = Board()
        for col in range(3):
            board.drop(col, "X")
        self.assertFalse(board.winner("X"))

    def test_invalid_and_full_column_do_not_change_board(self):
        board = Board()
        before = [row[:] for row in board.grid]
        self.assertIsNone(board.drop(-1, "X"))
        self.assertIsNone(board.drop(COLS, "X"))
        self.assertEqual(before, board.grid)

        for _ in range(ROWS):
            board.drop(0, "X")
        before = [row[:] for row in board.grid]
        self.assertIsNone(board.drop(0, "O"))
        self.assertEqual(before, board.grid)

    def test_full_board(self):
        board = Board()
        board.grid = [["X"] * COLS for _ in range(ROWS)]
        self.assertTrue(board.full())

        game = Game()
        game.board.grid = [
            list(".XOXOXX"),
            list("XXOXOOO"),
            list("OXXXOOX"),
            list("XOXOXOO"),
            list("XOXOXXO"),
            list("XXOXXXO"),
        ]
        output = io.StringIO()
        with patch.object(builtins, "input", side_effect=["1"]), redirect_stdout(output):
            game.run()
        self.assertIn("Draw.", output.getvalue())
        self.assertTrue(game.board.full())


class AITests(unittest.TestCase):
    def test_ai_takes_immediate_win(self):
        board = Board()
        for col in range(3):
            board.drop(col, "O")
        self.assertEqual(3, AI().choose_column(board))

    def test_ai_blocks_immediate_loss(self):
        board = Board()
        for _ in range(3):
            board.drop(4, "X")
        self.assertEqual(4, AI().choose_column(board))

    def test_ai_uses_only_legal_columns(self):
        board = Board()
        for col in range(COLS - 1):
            for _ in range(ROWS):
                board.drop(col, "X")
        self.assertEqual(COLS - 1, AI().choose_column(board))

    def test_ai_returns_none_on_full_board(self):
        board = Board()
        board.grid = [["X"] * COLS for _ in range(ROWS)]
        self.assertIsNone(AI().choose_column(board))


class GameTests(unittest.TestCase):
    def run_game(self, inputs):
        game = Game()
        output = io.StringIO()
        with patch.object(builtins, "input", side_effect=inputs), redirect_stdout(output):
            game.run()
        return game, output.getvalue()

    def test_quit(self):
        game, output = self.run_game(["q"])
        self.assertEqual(Board().grid, game.board.grid)
        self.assertNotIn("placed a disc", output)

    def test_invalid_input_does_not_change_board(self):
        game, output = self.run_game(["abc", "8", "q"])
        self.assertEqual(Board().grid, game.board.grid)
        self.assertIn("Enter a column number.", output)
        self.assertIn("Column unavailable.", output)

    def test_feedback_occurs_once_per_successful_move(self):
        game = Game()
        game.ai.choose_column = lambda _board: 6
        output = io.StringIO()
        with patch.object(builtins, "input", side_effect=["1", "q"]), redirect_stdout(output):
            game.run()
        self.assertEqual(2, output.getvalue().count("placed a disc"))

    def test_winning_move_ends_before_another_prompt(self):
        game = Game()
        for col in range(3):
            game.board.drop(col, "X")
        output = io.StringIO()
        with patch.object(builtins, "input", side_effect=["4"]) as mocked_input:
            with redirect_stdout(output):
                game.run()
        mocked_input.assert_called_once()
        self.assertIn("X wins!", output.getvalue())


if __name__ == "__main__":
    unittest.main()
