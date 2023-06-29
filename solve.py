PUZZLE_SIZE = 9
SQUARE_SIZE = int(PUZZLE_SIZE / 3)
MAX_ITERATIONS = 100

def copy_2d_array(arr):
    copy = []
    for r in range(0, len(arr)):
        row = [x for x in arr[r]]
        copy.append(row)
    return copy

def copy_2d_array_inverted(arr):
    inverted = []
    for c in range(0, PUZZLE_SIZE):
        col = []
        for r in range(0, PUZZLE_SIZE):
            col.append(arr[r][c])
        inverted.append(col)
    return inverted

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

                debug = False
                
                (row_r, row_c) = (r, c)
                in_row = [x for x in rows[row_r] if x != 0]

                (col_r, col_c) = row_to_col_coords((row_r, row_c))
                in_col = [x for x in cols[col_r] if x != 0]

                (square_r, square_c) = row_to_square_coords((row_r, row_c))
                in_square = [x for x in squares[square_r] if x != 0]

                possible_vals[r][c] = [x for x in possible_vals[r][c] if not x in in_row and not x in in_col and not x in in_square]

                if debug:
                    print("in row: " + str(in_row))
                    print("in col: " + str(in_col))
                    # print(cols[col_r])
                    print("in square: " + str(in_square))
                    print("possible: " + str(possible_vals[r][c]))
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


def pretty_print(puzzle):
    for row in puzzle:
        print(str(row))


# WORKS
TEST_PUZZLE_1 = [  
                    [0, 4, 5,   8, 7, 1,    0, 0, 6],
                    [0, 2, 6,   0, 4, 0,    0, 0, 1],
                    [0, 9, 0,   2, 5, 6,    4, 0, 0],

                    [9, 0, 0,   4, 0, 0,    5, 6, 0],
                    [2, 5, 4,   6, 0, 0,    1, 0, 0],
                    [6, 8, 0,   0, 0, 0,    3, 0, 0],

                    [4, 0, 9,   1, 3, 2,    6, 8, 0],
                    [1, 6, 0,   0, 0, 8,    0, 3, 4],
                    [0, 0, 8,   0, 0, 4,    2, 1, 0],
                ]

TEST_PUZZLE_2 = [   
                    [3, 0, 0,   0, 0, 9,    0, 0, 0],
                    [0, 0, 0,   0, 4, 0,    1, 0, 3],
                    [0, 7, 1,   0, 0, 0,    0, 4, 2],

                    [4, 1, 0,   3, 8, 0,    2, 9, 5],
                    [7, 8, 9,   4, 5, 0,    6, 0, 1],
                    [0, 0, 0,   6, 9, 0,    0, 7, 0],

                    [1, 6, 0,   0, 7, 5,    0, 0, 0],
                    [0, 0, 0,   0, 1, 0,    0, 2, 0],
                    [0, 9, 3,   0, 0, 4,    5, 0, 0],
                ]

solution = solve(TEST_PUZZLE_2)
print("Solved: " + str(solution[0]))
print("Iterations: " + str(solution[1]))
print("Remaining: " + str(solution[2]))
pretty_print(solution[3])
