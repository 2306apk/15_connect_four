# Scenario 15 — Connect Four vs AI

A terminal Connect Four game with a board module, a player turn loop, and a simple AI.

## Provided files

- `main.py` — entry point.
- `game.py` — turn handling and game flow.
- `board.py` — board state, drops, and win detection.
- `ai.py` — computer move selection.
- `requirements.txt` — dependency declaration.

## Setup

```bash
python main.py
```

## Before changing the code

Play several games, inspect all modules, and construct horizontal, vertical, and
diagonal winning positions. Trace how a move travels from the command line to the
board and then to winner detection.

## Task 1 — Complete win detection

Make win detection recognise every four-in-a-row direction, including both diagonals,
without breaking horizontal and vertical wins.

**Done when:** all four directions are detected and shorter sequences do not count.

## Task 2 — Complete game termination

Handle draws, full columns, invalid moves, and game termination consistently. A
winning move must stop the game before another turn is requested.

**Done when:** no invalid move changes the board and every terminal state is clear.

## Task 3 — Improve the AI

Add meaningful decision-making. The AI should take an immediate winning move when one
exists and block an immediate player win when necessary. Handle full columns safely.

**Done when:** the AI never selects an illegal column and responds correctly to one-move threats.

## Task 4 — Move-level feedback

Add concise feedback for a successful disc placement. It should occur once per actual
move, not once per cell inspected by win detection or AI analysis.

## Required testing

Test horizontal, vertical, both diagonals, draw positions, full columns, invalid input,
immediate AI wins, immediate AI blocks, and quitting.


## LLM usage

You may use an LLM during the lab. The goal is to use it as a coding assistant while
retaining responsibility for understanding and testing the result.

- Inspect the existing code before asking for changes.
- Ask for explanations when you do not understand a proposed change.
- Test generated code against the stated behaviour and edge cases.
- Keep your complete LLM chat history for submission.
- Do not replace the whole project with an unrelated implementation.
- Keep all state in memory; do not add CSV, JSON, SQLite, or other persistence.

## Submission checklist

- [x] Task 1 completed and the original defect was reproduced and fixed.
- [x] Tasks 2–4 completed and tested.
- [x] Boundary and invalid-input cases tested.
- [x] No unnecessary external dependencies added.
- [x] No persistent storage added.
- [x] Code remains understandable and modular.
- [x] Complete LLM chat-history link included.

## Folder structure

```text
scenario-03-connect-four/
├── README.md
├── requirements.txt
├── main.py
├── game.py
├── board.py
└── ai.py
```

## Submission Checklist

Submission is only the following three things:

- [x] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior: [`Lab-4/Videos/before.mp4`](Lab-4/Videos/before.mp4)
- [x] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working: [`Lab-4/Videos/after.mp4`](Lab-4/Videos/after.mp4)
- [x] The Chat/LLM used page link, with the complete chat history: [`Lab-4/Chat_History_Link.md`](Lab-4/Chat_History_Link.md)

The PDF export and verification record are available at [`Lab-4/Chat_History.pdf`](Lab-4/Chat_History.pdf).

The complete packaged submission is available at [`15_connect_four_Lab_4_Submission.zip`](15_connect_four_Lab_4_Submission.zip).
