def find_next_empty(puzzle):
    # finds the next row, col on the puzzle thats empty -> rep with -1
    # return row, col
    # using index 0-8 for location
    for r in range(9):
        for c in range(9):
           if puzzle[r][c] == -1:
              return r, c
    return None, None  #if theres no more empty space

def is_valid(puzzle,  guess, row, col):
    #figures out if the guess at that row/col if vaild or no, if Yes return true
    #start with row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    #col_vals = []
    #for i in range(9):
    #   col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False


#3x3 square, find the 3 values in that row and col of the square
    row_start = (row // 3) * 3 #1//3=0 , 5//3=1 ...
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
       for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                  return False

    return True





def solve_sudoku(puzzle):
    # solve sudoku using backtracking.

    # step1: choose somewhere on the puzzle to put in our guess.
    # helper function  passing the puzzle to find the open space on the board

    row, col = find_next_empty(puzzle)

    #step1.1: vaild input cheker
    if row is None:
        return True

    #step2: if there a place for a number, make a guess between 1-9
    for guess in range(1,10):
        #step3: chick if vaild guess
        if is_valid(puzzle, guess, row, col):

            puzzle[row][col] = guess #if this is vaild, place that guess on the puzzle
            # step4: recurse call the function
            if solve_sudoku(puzzle):
                return True
        #step5: if not vaild or our guess does not solve the puzzle
        #backtrack and try a new number
        puzzle[row][col] = -1 #reset the guess

    #step6: in none of the number that we try work, then this puzzle is unslove
    return False
#step7: sudokue puzzle as an input to solve
def get_sudoku_input():
    board = []
    print("Enter your Sudoku puzzle row by row. Use -1 for empty cells.")
    print("Each row should have 9 numbers separated by spaces.")
    for i in range(9):
        while True:
            row_input = input(f"Row {i+1}: ")
            try:
                row = [int(x) for x in row_input.strip().split()]
                if len(row) == 9:
                    board.append(row)
                    break
                else:
                    print("⚠️ Each row must have exactly 9 numbers.")
            except ValueError:
                print("⚠️ Invalid input. Use numbers only.")
    return board


if __name__ == '__main__':
    board = get_sudoku_input()
    print("\nSolving Sudoku...\n")
    print(solve_sudoku(board))
    print("Solved Board:")
    for row in board:
        print(row)