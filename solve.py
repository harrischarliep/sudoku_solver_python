from constants import PUZZLE_SIZE, SQUARE_SIZE, MAX_ITERATIONS
from utils import copy_2d_array, copy_2d_array_inverted

get_rows = copy_2d_array
get_cols = copy_2d_array_inverted
def get_squares(arr):
    square_arr = []
    for sr in range(0, SQUARE_SIZE):
        for sc in range(0, SQUARE_SIZE):
            init_r = sr * SQUARE_SIZE
            init_c = sc * SQUARE_SIZE
            square = []
            for r in range(init_r, init_r + SQUARE_SIZE):
                for c in range(init_c, init_c + SQUARE_SIZE):
                    square.append(arr[r][c])
            square_arr.append(square)
    return square_arr

def row_to_col_coords(row_coords):
    (row_r, row_c) = row_coords
    return (row_c, row_r)

def row_to_square_coords(row_coords):
    (row_r, row_c) = row_coords
    quot_r = int(row_r / SQUARE_SIZE)
    quot_c = int(row_c / SQUARE_SIZE)
    square_r = (quot_r * SQUARE_SIZE) + quot_c

    rem_r = row_r % SQUARE_SIZE
    rem_c = row_c % SQUARE_SIZE
    square_c = (rem_r * SQUARE_SIZE) + rem_c

    return (square_r, square_c)

def init_possible_vals(rows):
    all_possible_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_vals = []
    remaining = PUZZLE_SIZE ** 2
    for r in range(0, PUZZLE_SIZE):
        row = []
        for c in range(0, PUZZLE_SIZE):
            val = rows[r][c]
            col = []
            if val != 0:
                col = [val]
                remaining -= 1
            else:
                col = [x for x in all_possible_vals]
            row.append(col)
        possible_vals.append(row)

    return (possible_vals, remaining)

def solve(puzzle):
    rows = get_rows(puzzle)
    cols = get_cols(puzzle)
    squares = get_squares(puzzle)

    (possible_vals, remaining) = init_possible_vals(rows)
    solved = False
    iteration = 0
    while not solved and iteration < MAX_ITERATIONS:
        for r in range(0, PUZZLE_SIZE):
            for c in range(0, PUZZLE_SIZE):
                if len(possible_vals[r][c]) == 1:
                    continue
                
                (row_r, row_c) = (r, c)
                in_row = [x for x in rows[row_r] if x != 0]

                (col_r, col_c) = row_to_col_coords((row_r, row_c))
                in_col = [x for x in cols[col_r] if x != 0]

                (square_r, square_c) = row_to_square_coords((row_r, row_c))
                in_square = [x for x in squares[square_r] if x != 0]

                possible_vals[r][c] = [x for x in possible_vals[r][c] if not x in in_row and not x in in_col and not x in in_square]
                if len(possible_vals[r][c]) == 1:
                    val = possible_vals[r][c][0]
                    rows[row_r][row_c] = val
                    cols[col_r][col_c] = val
                    squares[square_r][square_c] = val
                    print("Found: " + str(val) + " at (" + str(row_r) + ", " + str(row_c) + ")")
                    remaining -= 1
    
        solved = remaining == 0
        iteration += 1
    
    return (solved, iteration, remaining, rows)
