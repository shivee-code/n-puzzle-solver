# N-Puzzle Solver

A Python implementation of an N-Puzzle solver using A* search with the Manhattan distance heuristic.

## Features

- Supports 3x3 to 5x5 puzzles
- Finds shortest sequence of moves to solve the puzzle
- Detects unsolvable states

## Input

- First line: integer `k` (board size)
- Next `k*k` lines: tile numbers (0 represents the empty space)

## Output

- First line: number of moves
- Following lines: moves (`UP`, `DOWN`, `LEFT`, `RIGHT`)

## Usage

Run with input file:

```bash
python3 solver.py < input.txt

```
## License

This project is licensed under the MIT License.

