from Sudoku_Site_Scraper import go_to_site

sudoku_board = []
pre_solution = []
solved_board = []


def get_sudoku_board(generated_board):
    for i in generated_board:
        sudoku_board.append(i)


def find_empty_locations(board):
    for i in board:
        for j in i:
            if j == 0:
                return board.index(i), i.index(j)
    return ""


def find_empty(board):
    for i in board:
        for j in enumerate(i):
            if j[1] == 0:
                pre_solution.append((board.index(i), j[0]))


def attempt_entry(board):
    position = find_empty_locations(board)
    if position == "":
        return True
    else:
        for entry in range(1, 10):
            if validate_position(board, entry, position):
                board[position[0]][position[1]] = entry

                if attempt_entry(board):
                    return True
                board[position[0]][position[1]] = 0
    return False


def validate_position(board, number, position):
    for row in range(len(board[0])):
        if board[position[0]][row] == number and position[1] != row:
            return False

    for column in range(len(board)):
        if board[column][position[1]] == number and position[0] != column:
            return False

    x_cord = position[1] // 3
    y_cord = position[0] // 3

    for i in range(y_cord * 3, (y_cord * 3) + 3):
        for j in range(x_cord * 3, (x_cord * 3) + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


def board_solution(generated):
    get_sudoku_board(generated)
    find_empty(sudoku_board)
    attempt_entry(sudoku_board)
    print('\n+++++++++++++++++++++++++++++++++++++\n')
    for i in sudoku_board:
        solved_board.append(i)

    return solved_board
