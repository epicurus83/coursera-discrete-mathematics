from week2_mathematical_thinking.diagonals_problem.utils import convert_board_to_string

solutions = []


def determines_diagonals_solutions(board=None, board_length=0, diagonals_num=0):
    """Determines arrangement of diagonals which can fit in a square board.
    The number of diagonals to be fitted in the board is given as a parameter.
    TODO Make program smart enough to determine the maximum number of diagonals itself.
    The algorithm is a backtracking algorithm.
    Right diagonal going from bottom left to top right = "/"
    Left diagonal going from bottom right to top left = "\"
    Empty space which contains no diagonal = "_"
    Unallocated cell = "-1"

    Args:
        board (:obj:`list`, optional): The square board object. Default to None.
        board_length(int, optional): The dimension of the board. Default to 0.
        diagonals_num(int, optional): The number of diagonals to be fitted in the board. Default to 0.

    Returns:
        List of solutions.

    """

    global solutions
    solutions = []

    if board is not None and type(board) != list:
        print("board must of type list or not defined.")
        return

    if type(board_length) != int:
        print("n must of type int or not defined.")
        return

    if board is None:
        board = [[]]

    _populate_board(board, board_length, 0, diagonals_num)
    return solutions


def _populate_board(board, board_length, current_diagonal_num, target_diagonal_num):
    _print_board(board)
    print('current diag num = ' + str(current_diagonal_num))
    if current_diagonal_num == target_diagonal_num and _is_board_complete(board, board_length):
        _add_solution(board)
        global solutions
        solutions.insert(len(solutions), board)
        # print('Solution = ' + convert_solutions_to_string(solutions))

    for char in ['\\', '/', '_']:
        x = len(board) - 1
        y = len(board[x])
        # print('y = ' + str(y))
        # print('x = ' + str(x))
        # print('board_len = ' + str(board_length))
        if y == board_length:
            if x == board_length - 1:
                continue
            board.append([])
            x += 1
            y = 0

        board[x].append(char)
        if can_extend_to_solution(board, x, y):
            if _is_diagonal(char):
                current_diagonal_num += 1
            _populate_board(board, board_length, current_diagonal_num, target_diagonal_num)
        else:
            board[x].pop()


def _is_board_complete(board, board_length):
    if len(board) != board_length:
        return False
    for x in range(len(board)):
        if len(board[x]) != board_length:
            return False
    return True


def _add_solution(board):
    global solutions
    for solution in solutions:
        for x in range(len(solution)):
            for y in range(len(solution[x])):
                if board[x][y] != solution[x][y]:
                    solutions.insert(len(solutions), solution)
                    return


def _is_diagonal(char):
    return char in ['\\', '/']


def _print_board(board):
    print(convert_board_to_string(board))


def can_extend_to_solution(board, x, y):
    _new_tile_value = board[x][y]
    if _new_tile_value == "/":
        if _is_right_diagonal_invalid(board, x, y):
            return False
    elif _new_tile_value == "\\":
        if _is_left_diagonal_invalid(board, x, y):
            return False
    return True


def _is_right_diagonal_invalid(board, x, y):
    return _check_left(board, x, y, "\\") or \
           _check_top(board, x, y, "\\") or \
           _check_top_right_is_right_diagonal(board, x, y) or \
           _check_bottom_left_is_right_diagonal(board, x, y)


def _check_left(board, x, y, value):
    return y > 0 and board[x][y - 1] == value


def _check_top(board, x, y, value):
    return x > 0 and board[x - 1][y] == value


def _check_top_right_is_right_diagonal(board, x, y):
    return x > 0 and y < len(board[x]) - 1 and board[x - 1][y + 1] == "/"


def _check_bottom_left_is_right_diagonal(board, x, y):
    return y > 0 and x < len(board) - 1 and board[x + 1][y - 1] == "/"


def _is_left_diagonal_invalid(board, x, y):
    return _check_left(board, x, y, "/") or \
           _check_top(board, x, y, "/") or \
           _check_bottom_right_is_right_diagonal(board, x, y) or \
           _check_top_left_is_right_diagonal(board, x, y)


def _check_bottom_right_is_right_diagonal(board, x, y):
    return x < len(board) - 1 and y < len(board[x]) - 1 and board[x + 1][y + 1] == "\\"


def _check_top_left_is_right_diagonal(board, x, y):
    return x > 0 and y > 0 and board[x - 1][y - 1] == "\\"
