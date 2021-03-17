def convert_board_to_string(board):
    board_str = '\n[\n'
    for x in range(len(board)):
        board_str += '\t['
        board_str += ', '.join(board[x])
        board_str += ']\n'
    board_str += ']'
    return board_str


def convert_solutions_to_string(solutions):
    solutions_str = '\n'
    for solution in solutions:
        solutions_str += convert_board_to_string(solution)
    return solutions_str
