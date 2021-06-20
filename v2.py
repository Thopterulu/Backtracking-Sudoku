from a_sudoku import SUDOKU_1
from checks import Checker

def check_empty(puzzle):
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == -1:
                return x, y
    return None, None

def solve_sudoku(puzzle):
    x,y = check_empty(puzzle)
    if x == None:
        return puzzle

    check = Checker(x, y)
    possible_values = check.full_check(puzzle)
    if len(possible_values) > 0:
        puzzle[y][x] = possible_values[0]
    else:
        break



if __name__ == "__main__":
    for a_row in SUDOKU_1:
        print(a_row)
    solved_sudoku = solve_sudoku(SUDOKU_1)
    for a_row in solved_sudoku:
        print(a_row)