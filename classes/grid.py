from classes.square import Square

import random
import time


class Grid:
    def __init__(self, level):
        self.level = level
        self.grid = []

    def init_grid(self):
        range_grid_size = range(0, 9)
        must_generate = True
        while must_generate:
            must_generate = False
            ts = time.time()
            # make sure to reset if grid was stuck and needed to be generated again
            self.grid = []
            # grid full of 0
            for _ in range_grid_size:
                row = [0 for _ in range_grid_size]
                self.grid.append(row)
            # Replacing all the 0 by good values
            for r in range_grid_size:
                should_restart = True
                while should_restart:
                    should_restart = False
                    if time.time() > ts + 2:
                        print("Grid is stuck, generating a new one...")
                        must_generate = True
                        break
                    for c in range_grid_size:
                        self.grid[r][c] = 0
                        int_available = [i for i in range(1, 10)]
                        while self.grid[r][c] == 0:
                            random_int = random.choice(int_available)
                            coordinates = (r, c)
                            is_not_in_col = self.check_column(coordinates, random_int)
                            is_not_in_square_fam = self.check_square_family(coordinates, random_int)
                            if random_int not in self.grid[r] and is_not_in_col and is_not_in_square_fam:
                                self.grid[r][c] = random_int
                            else:
                                int_available.remove(random_int)
                            if len(int_available) == 0:
                                should_restart = True
                                break
                        if should_restart:
                            break
                if must_generate:
                    break

    def check_column(self, coordinates, randint):
        row, col = coordinates
        same_number = True
        prev_rows = range(0, row)
        next_rows = range(row, 9)
        for row_pos in prev_rows:
            if self.grid[row_pos][col] == randint:
                same_number = False
        if not same_number:
            return same_number
        for row_pos in next_rows:
            if self.grid[row_pos][col] == randint:
                same_number = False
        return same_number

    def check_square_family(self, coordinates, randint=None):
        related_square = []
        for square in self.build_squares_coordinates():
            if coordinates in square:
                related_square = square
        related_square.remove(coordinates)
        related_square_values = [self.grid[r][c] for r, c in related_square]
        if randint in related_square_values:
            return False
        else:
            return True

    def build_squares_coordinates(self):
        squares = []

        r_min, r_max = 0, 3

        for _ in range(0, 3):
            s1 = []
            s2 = []
            s3 = []
            for r in range(r_min, r_max):
                for c in range(0, 3):
                    s1.append((r, c))
                for c in range(3, 6):
                    s2.append((r, c))
                for c in range(6, 9):
                    s3.append((r, c))
            squares.append(s1)
            squares.append(s2)
            squares.append(s3)
            r_min += 3
            r_max += 3

        return squares


    def print_grid(self):
        for row in self.grid:
            print(f"{row}")
