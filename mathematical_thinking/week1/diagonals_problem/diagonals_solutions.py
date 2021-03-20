from mathematical_thinking.week1.diagonals_problem.utils import print_board

solution = []


def determines_diagonals_solutions(perm=None, board_len=0, diagonals_num=0):
    """Determines first solution for arrangement of diagonals which can fit in a square board.
    The number of diagonals to be fitted in the board is given as a parameter.
    The board will be represented as a 1 dimensional list for simplicity.
    TODO Make program smart enough to determine the maximum number of diagonals itself.
    TODO Make program faster for 5 sided.
    The algorithm is a backtracking algorithm.
    Right diagonal going from bottom left to top right = "/"
    Left diagonal going from bottom right to top left = "\"
    Empty space which contains no diagonal = "_"

    Args:
        perm (:obj:`list`, optional): The square board object represented as permutation. Default to None.
        board_len(int, optional): The dimension of the board. Default to 0.
        diagonals_num(int, optional): The number of diagonals to be fitted in the board. Default to 0.

    Returns:
        First solution found.

    """

    if perm is not None and type(perm) != list:
        print("board must of type list or not defined.")
        return

    if type(board_len) != int:
        print("n must of type int or not defined.")
        return

    if perm is None:
        perm = []

    global solution
    solution = []

    _populate_board(perm, board_len, 0, diagonals_num)

    return solution


def _populate_board(perm, board_len, current_diagonal_num, target_diagonal_num):
    if current_diagonal_num == target_diagonal_num and _board_is_complete(perm, board_len):
        solution.append(perm.copy())

    if len(solution) > 0:
        return

    for char in ['/', '\\', '_']:
        if _board_is_complete(perm, board_len):
            continue
        perm.append(char)
        if _is_diagonal(char):
            current_diagonal_num += 1
        if can_extend_to_solution(perm, board_len):
            _populate_board(perm, board_len, current_diagonal_num, target_diagonal_num)
        current_diagonal_num -= 1
        perm.pop()


def _board_is_complete(perm, board_length):
    return len(perm) == board_length * board_length


def _is_diagonal(char):
    return char in ['\\', '/']


def can_extend_to_solution(perm, board_len):
    _new_val = perm[len(perm) - 1]
    if _new_val == '/':
        return _is_right_diagonal_valid(perm, board_len)
    if _new_val == '\\':
        return _is_left_diagonal_valid(perm, board_len)
    return True


def _is_right_diagonal_valid(perm, board_len):
    return _check_left_valid(perm, board_len, '\\') and \
           _check_top_valid(perm, board_len, '\\') and \
           _check_top_right_valid(perm, board_len, '/')


def _check_left_valid(perm, board_len, invalid_val):
    _perm_len = len(perm)
    _left_val_index = _perm_len - 2
    if _left_val_index < 0 or (_left_val_index + 1) % board_len == 0:
        return True
    return perm[_left_val_index] != invalid_val


def _check_top_valid(perm, board_len, invalid_val):
    _perm_len = len(perm)
    _top_val_index = _perm_len - board_len - 1
    if _top_val_index < 0:
        return True
    return perm[_top_val_index] != invalid_val


def _check_top_right_valid(perm, board_len, invalid_val):
    _perm_len = len(perm)
    _top_right_val_index = _perm_len - board_len
    if _top_right_val_index < 1:
        return True
    return perm[_top_right_val_index] != invalid_val


def _is_left_diagonal_valid(perm, board_len):
    return _check_left_valid(perm, board_len, '/') and \
           _check_top_valid(perm, board_len, '/') and \
           _check_top_left_valid(perm, board_len, '\\')


def _check_top_left_valid(perm, board_len, invalid_val):
    _perm_len = len(perm)
    if _perm_len % board_len == 1:
        return True
    _top_left_val_index = _perm_len - board_len - 2
    if _top_left_val_index < 0:
        return True
    return perm[_top_left_val_index] != invalid_val
