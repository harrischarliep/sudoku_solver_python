from solve import solve

def pretty_print(puzzle):
    for row in puzzle:
        print(str(row))

# SOLVES
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

# PARTIALLY SOLVES
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
