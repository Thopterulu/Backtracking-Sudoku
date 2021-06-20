from a_sudoku import SUDOKU_1

def column_value_chooser(puzzle: list, y_axis: int, x_axis: int, list_values: list):
    # choisit la valeur en fonction des valeurs précendentes dans la collumn
    # a cet endroit on peut choisir d'être "plus intelligent" et de prendre en compte des nombre qui arrivent plus loin dans la collumn
    # mais pour des raisons de strict brute force je vais juste prendre en compte les valeurs passées
    for i in range(0, y_axis):
        if puzzle[i][x_axis] in list_values:
            list_values.remove(puzzle[i][x_axis])
    if len(list_values) == 0:
        return False
    return list_values[0]

def fill_empty_cell(puzzle: list, y_axis: int, x_axis: int, list_values: list) -> tuple:
    """If my cell is empty I fill it with the first value of my list.

    Args:
        list_values (list): List of possible values.

    Returns:
        tuple(int, list): next value, list of value - next value
    """
    next_value = column_value_chooser(puzzle, y_axis, x_axis, list_values)
    list_values.remove(next_value)
    return next_value, list_values

def pick_number_forward(puzzle: list, y_axis: int, x_axis: int, cell_value: int, list_values: list) -> tuple:
    if cell_value == -1:
        return fill_empty_cell(puzzle, y_axis, x_axis, list_values)
    if cell_value in list_values:
        list_values.remove(cell_value)
        return cell_value, list_values
    else:
        # time to go back in the cells.
        list_values.append(cell_value)
        return cell_value, list_values

def pick_number_backward(cell_value: int, list_values: list) -> tuple:
    if cell_value in list_values:
        next_value = list_values[0]
        list_values.pop(0)
        return next_value, list_values
    list_values.append(cell_value)
    return cell_value, list_values

def solve_sudoku(sudoku: list):
    start_x, start_y = 0, 0
    list_values = [1,2,3,4,5,6,7,8,9]
    return progress_in_sudoku(start_x, start_y, list_values, sudoku)


def progress_in_sudoku(x_axis: int, y_axis: int, list_values: list, sudoku: list, backing=False):
    if x_axis < 9 and y_axis < 9:
        if backing:
            sudoku[y_axis][x_axis], list_values = pick_number_backward(sudoku[y_axis][x_axis], list_values)
        else:
            sudoku[y_axis][x_axis], list_values = pick_number_forward(sudoku, y_axis, x_axis, sudoku[y_axis][x_axis], list_values)
        if sudoku[y_axis][x_axis] in list_values:
            return progress_in_sudoku(x_axis - 1, y_axis, list_values, sudoku, True)
        return progress_in_sudoku(x_axis + 1, y_axis, list_values, sudoku)
    elif y_axis < 9:  # change row
        list_values = [1,2,3,4,5,6,7,8,9]
        return progress_in_sudoku(0, y_axis + 1, list_values, sudoku)
    return sudoku



if __name__ == "__main__":
    back_tacking_sudoku = []
    for a_row in SUDOKU_1:
        print(a_row)
    #solution = progress_in_sudoku(SUDOKU_1, back_tacking_sudoku)
    #print(solution)
    solved_sudoku = solve_sudoku(SUDOKU_1)
    for a_row in solved_sudoku:
        print(a_row)


