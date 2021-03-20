def convert_solutions_to_string(solutions, board_len):
    solutions_str = '\n'
    for solution in solutions:
        solutions_str += convert_perm_to_string(solution, board_len)
    return solutions_str


def print_board(perm, board_len):
    print(convert_perm_to_string(perm, board_len))


def convert_perm_to_string(perm, board_len):
    _perm_str = ''
    for i in range(len(perm)):
        _perm_str += str(perm[i])
        _perm_str += ' ' if (i + 1) % board_len != 0 else '\n'
    _perm_str += '\n'
    return _perm_str
