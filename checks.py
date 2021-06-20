class Checker:
    def __init__(self, current_x: int, current_y: int) -> None:
        self.possible_values=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.current_x = current_x
        self.current_y = current_y
        self.squares = {"square_1": {"x": [0,1,2],
                                     "y": [0,1,2]},
                        "square_2": {"x": [3,4,5],
                                     "y": [0,1,2]},
                        "square_3": {"x": [6,7,8],
                                     "y": [0,1,2]},
                        "square_4": {"x": [0,1,2],
                                     "y": [3,4,5]},
                        "square_5": {"x": [3,4,5],
                                     "y": [3,4,5]},
                        "square_6": {"x": [6,7,8],
                                     "y": [3,4,5]},
                        "square_7": {"x": [0,1,2],
                                     "y": [6,7,8]},
                        "square_8": {"x": [3,4,5],
                                     "y": [6,7,8]},
                        "square_9": {"x": [6,7,8],
                                     "y": [6,7,8]}
        }

    def check_row(self, puzzle:list):
        for value in puzzle[self.current_y]:
            if value != -1 and value in self.possible_values:
                self.possible_values.remove(value)

    def check_column(self, puzzle:list):
        for y in range(9):
            if puzzle[y][self.current_x] != -1 and puzzle[y][self.current_x] in self.possible_values:
                self.possible_values.remove(puzzle[y][self.current_x])

    def check_square(self, puzzle:list):
        # define squares
        current_square = self.find_current_square()
        for y_value in range(current_square["y"][0], current_square["y"][2]+ 1):
            for x_value in range(current_square["x"][0], current_square["x"][2]+ 1):
                if puzzle[y_value][x_value] != -1 and puzzle[y_value][x_value] in self.possible_values:
                    self.possible_values.remove(puzzle[y_value][x_value])

    def find_current_square(self):
        for a_square in self.squares:
            if self.current_x in self.squares[a_square]["x"] and self.current_y in self.squares[a_square]["y"]:
                return self.squares[a_square]
        return None

    def full_check(self, puzzle: list):
        self.check_row(puzzle)
        self.check_column(puzzle)
        self.check_square(puzzle)
        return self.possible_values