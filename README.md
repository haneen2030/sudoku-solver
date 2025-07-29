## 🧩 Sudoku Solver in Python

A backtracking Sudoku solver written in Python.  
You can input your own puzzle through the terminal and get the solved version in seconds.

---

##  Features

- Accepts user input row-by-row (with `-1` for empty cells)
- Uses backtracking algorithm to solve the puzzle
- Shows the solved board if a solution exists

---

## How to Use

### 1. Clone the repository
```bash
git clone https://github.com/haneen2030/sudoku-solver.git
cd sudoku-solver

### 2. Run the solver
Make sure you have Python installed (Python 3.x)
```bash
python sudoku_solver.py
### 3. Enter the puzzle
You'll be asked to type the puzzle row by row.
Use -1 for empty cells, and enter 9 numbers separated by spaces, like this:

Row 1: 3 9 -1 -1 5 -1 -1 -1 -1
Row 2: -1 -1 -1 2 -1 -1 -1 -1 5
...

Example Output

Solving Sudoku...

True
Solved Board:
[3, 9, 4, 8, 5, 1, 7, 6, 2]
[7, 1, 8, 2, 6, 9, 3, 5, 4]
...

