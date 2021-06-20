from a_sudoku import SUDOKU_1
from checks import Checker
from just_checking import is_valid

def check_empty(puzzle):
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == -1:
                return x, y
    return None, None

def solve_sudoku(puzzle):
    x,y = check_empty(puzzle)
    if x == None:
        return True

    for i in range(1, 10):
        possible_values = Checker(x, y).full_check(puzzle)
        if i in possible_values:
            puzzle[y][x] = i
            if solve_sudoku(puzzle):
                return True
        puzzle[y][x] = -1

    return False




if __name__ == "__main__":
    for a_row in SUDOKU_1:
        print(a_row)
    print("\n\n")
    print(solve_sudoku(SUDOKU_1))
    for a_row in SUDOKU_1:
        print(a_row)